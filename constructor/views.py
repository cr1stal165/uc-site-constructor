from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse


def index(request):
    return render(request, "constructor.html")


def take_color(request):
    return render(request, "take_color.html")


def template_uc1(request):
    return render(request, "template_uc1.html")