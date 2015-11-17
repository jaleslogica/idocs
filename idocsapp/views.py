from django.shortcuts import render

from idocsapp.models import Question
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")

def proposta(request):
    return render(request, "proposta.html")

def empresa(request):
    return render(request, "empresa.html")

def download(request):
    return render(request, "download.html")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)