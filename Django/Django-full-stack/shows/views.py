from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Show


def shows(request):
    context = {
        "all_shows": Show.objects.all()
    }
    return render(request, "application/shows.html", context)


def shows_new(request):
    if request.method == 'POST':
        Show.objects.create(title = request.POST['title'], network = request.POST['network'], release_date = request.POST['release_date'])
    return render(request, "application/shows_new.html")


def shows_edit(request, my_val):
    shows = Show.objects.get(id = my_val)
    context = {
        "show": Show.objects.get(id = my_val)
    }
    return render(request, "application/shows_edit.html", context)

def process_edit(request, my_val):
    if request.method == 'POST':
        show = Show.objects.get(id = my_val)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.save()
    return redirect(f"/shows/{my_val}")


def show_one(request, my_val):
    shows = Show.objects.get(id = my_val)
    context = {
        "show": Show.objects.get(id = my_val)
    }
    return render(request, "application/show_one.html", context)


def addnew(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/shows/new")
    
    else:
        new_show = Show.objects.create(title=request.POST["title"], network=request.POST["network"], release_date=request.POST["release_date"])
        new_show_id = new_show.id
        messages.success(request, "Show successfully added.")
        return redirect("/shows")


def destroy(request, id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect("/shows")

