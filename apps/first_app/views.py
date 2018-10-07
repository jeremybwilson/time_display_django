from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import strftime
import re, datetime

def index(request):
    if 'logged_in' not in request.session:
        request.session['logged_in'] = False
        print "Session 'logged_in' status was not stored, so we set( it to: " + str(request.session['logged_in'])
    else:
        print "Session 'logged_in' status already stored as: " + str(request.session['logged_in'])

    if 'session_counter' not in request.session:
        request.session['session_counter'] = 0

    # now = datetime.datetime.now()
    todaysDateVariable = datetime.datetime.now().date()
    time = strftime("%H:%M %p")
    context = {
        'todaysDateVariable': todaysDateVariable,
        'time': time,
    }

    print "*" * 60
    request.session['session_counter'] += 1
    print request.session['session_counter']

    return render(request, 'first_app/index.html', context)
