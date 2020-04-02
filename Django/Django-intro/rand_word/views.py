from django.shortcuts import render, redirect
import random

def index(request):
    return render(request, "application/index.html")

def random_word(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1
    word = ''
    letters = ['A', 'b', 'C', 'd', 'E', 'f', 'G', 'h', 'I', 'j']
    for times in range (0, 10):
        word = word + str(random.choice(letters))
    r_words = {'random_word': word}
    return render(request, 'application/index.html', r_words)

def reset(request):
    request.session.clear()
    return redirect('/')