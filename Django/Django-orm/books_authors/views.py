from django.shortcuts import render, HttpResponse, redirect
from .models import Author
from .models import Book

def main(request):
    context = {
        "all_books": Book.objects.all()
    }
    return render(request, "books_authors_app/main.html", context)

def addbook(request):
    if request.method == 'POST':
        Book.objects.create(title = request.POST['title'],desc = request.POST['description']),
    return redirect("/")

def authors(request):
    context = {
        "all_authors": Author.objects.all()
    }
    return render(request, "books_authors_app/authors.html", context)

def addauthor(request):
    if request.method == 'POST':
        Author.objects.create(first_name = request.POST['fname'], last_name = request.POST['lname'], notes = request.POST['notes'] ),
    return redirect("/authors")

def onebook(request, my_val):
    books = Book.objects.get(id = my_val)
    all_authors = Author.objects.all()
    context = {
        "book": Book.objects.get(id = my_val),
        "all_books": books.books_authors.all(),
        "all_authors": all_authors
    }
    return render(request, "books_authors_app/onebook.html", context)

def oneauthor(request, my_val):
    this_author =  Author.objects.get(id = my_val)
    all_books = Book.objects.all()
    context = {
        "author": Author.objects.get(id = my_val),	
        "this_author": this_author.books.all(),
        "all_books": all_books
    }
    return render(request, "books_authors_app/oneauthor.html", context)

def getbook(request, my_val):
    if request.method == 'POST':
        book = Book.objects.get(id = my_val)
        author = Author.objects.get(id = request.POST['authorid'])
        book.books_authors.add(author)
    return redirect("/book/" + str(my_val))

def getauthor(request, my_val):
    if request.method == 'POST':
        this_author = Author.objects.get(id = my_val)	
        book = Book.objects.get( id = request.POST['book'])
        this_author.books.add(book)
    return redirect("/author/" + str(my_val))
