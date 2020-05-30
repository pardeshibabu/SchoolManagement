import os

from django.shortcuts import render
from django.views import generic


class ProfilePage(generic.TemplateView):
    '''
    Account Profile Page
    '''


def index(request):
    return render(request, template_name='index.html')


def blog(request):
    return render(request, template_name='blog.html')


def blog_single(request):
    return render(request, template_name='blog-dingle.html')


def contact(request):
    return render(request, template_name='contact.html')


def cources(request):
    return render(request, template_name='courses.html')


def pricing(request):
    return render(request, template_name='pricing.html')


def teacher(request):
    return render(request, template_name='teacher.html')
