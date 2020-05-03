from django.shortcuts import render
from django.views import generic


class ProfilePage(generic.TemplateView):
    '''
    Account Profile Page
    '''


def index(request):
    return render(request, template_name='base.html')
