from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome!! pybo에 오신 것을 환영합니다.")
