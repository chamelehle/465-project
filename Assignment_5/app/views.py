from django.http import HttpResponse, JsonResponse, Http404, HttpRequest
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404
from django.utils.html import escape
from django.http import JsonResponse
import json as simplejson
from django.views.decorators.csrf import csrf_exempt

from .forms import *
from .models import *

@csrf_exempt
def comments(request):
    if request.method == "GET":
        submits = submit.objects.all()
        submission = {}
        submission['submits']=[]
        for j in submits:
            submission['submits']+=[{
                'comment':submit.comment
                }]
        return JsonResponse(submission)
    if request.method == 'POST':
        return HttpResponse("POST successful")
    return HttpResponse("404")

def home(request):
    return render(
        request,
        'foundation/index.html'
     )
def events(request):
    form = SubmitForm
    if request.method == "POST":
        form = SubmitForm(request.POST)
        if form.is_valid():
            dat = form.cleaned_data
            suggested = submit(
                date=escape(dat['date']),
                name=escape(dat['user_name']),
                comment=escape(dat['user_input']))
            suggested.save()
    array = []
    suggestList = submit.objects.all()

    for i in suggestList:
        array += [(i.name, i.date, i.comment)]

    context = {
        "submit":array,
        'form':form,
        }

    return render(
        request,
        'foundation/events.html',
        context
     )
def about(request):
    form = AboutForm
    if request.method == "POST":
        form = AboutForm(request.POST)
        if form.is_valid():
            dat = form.cleaned_data
            about_page = aboutl(
                email=escape(dat['date']),
                person_name=escape(dat['user_name']),
                position=escape(dat['user_input']),
                phone=escape(dat['phone_num']))
            about_page.save()
    array = []
    suggestList = aboutl.objects.all()

    for i in suggestList:
        array += [(i.person_name, i.email, i.position, i.phone)]

    context = {
        "aboutl":array,
        'form':form,
        }

    return render(
        request,
        'foundation/about.html',
        context
     )
def map(request):
    return render(
        request,
        'foundation/map.html',
        context
     )
def login(request):
    return render(
        request,
        'foundation/login.html',
        context
     )
def facts(request):
    form = FactForm
    if request.method == "POST":
        form = FactForm(request.POST)
        if form.is_valid():
            dat = form.cleaned_data
            facted = fact(
                url=escape(dat['date']),
                title=escape(dat['user_name']),
                description=escape(dat['user_input']))
            facted.save()
    array = []
    suggestList = fact.objects.all()

    for i in suggestList:
        array += [(i.title, i.url, i.description)]

    context = {
        "fact":array,
        'form':form,
        }

    return render(
        request,
        'foundation/facts.html',
        context
     )
