from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import localtime, strftime, gmtime
from datetime import datetime
from .models import *
import bcrypt
import re


def index(request):
    return render(request, "application/index.html")

def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else: 
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pw_hash )
        user = User.objects.last()
        request.session['logged_in'] = user.id
        return redirect("/books")
    return redirect('/')


def login(request):
    errors = User.objects.loginValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else: 
        user = User.objects.get(email=request.POST['log_email'])
        request.session['logged_in'] = user.id
        return redirect('/books')
    return redirect('/')


def books(request):
    context = {
        'user': User.objects.get(id=request.session['logged_in']), 
        'all_books': Book.objects.all(), 
    }
    return render(request, 'application/books.html', context)


def addbook(request):
    errors = Book.objects.bookValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)

    user = User.objects.get(id=request.session['logged_in'])
    book = Book.objects.create(title = request.POST['title'], desc = request.POST['desc'], uploader = User.objects.get(id=request.session['logged_in']))
    book.liked_users.add(user)
    return redirect("/books")


def uploaded(request, my_val):
    context = {
        'user': User.objects.get(id=request.session['logged_in']), 
        'book': Book.objects.get(id = my_val), 
        'date': strftime("%b %d, %Y", localtime()),
        'time': strftime('%-I:%M %p', localtime())
    }
    return render (request, 'application/uploaded.html', context)


def update(request, my_val):
    book = Book.objects.get(id = my_val)
    book.title = request.POST.get('title')
    book.desc = request.POST.get('desc')
    book.save()
    return redirect(f"/books/{my_val}")


def logout(request):
    request.session['logged_in'] = None
    messages.error(request, "You have successfully logged out")
    return redirect('/')

def destroy(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect("/books")


def add_fave(request, my_val):
    user = User.objects.get(id=request.session['logged_in'])
    book = Book.objects.get(id = my_val)
    book.liked_users.add(user)
    return redirect('/books')


def add_fav(request, my_val):
    user = User.objects.get(id=request.session['logged_in'])
    book = Book.objects.get(id = my_val)
    book.liked_users.add(user)
    return redirect(f"/books/{my_val}")


def un_fave(request, my_val):
    user = User.objects.get(id=request.session['logged_in'])
    book = Book.objects.get(id = my_val)
    book.liked_users.remove(user)
    return redirect(f"/books/{my_val}")