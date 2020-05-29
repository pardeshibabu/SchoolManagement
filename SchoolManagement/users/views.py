import os

from django.shortcuts import render
from django.views import generic


class ProfilePage(generic.TemplateView):
    '''
    Account Profile Page
    '''


def index(request):
    # import ipdb
    # ipdb.set_trace()
    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # STATIC_URL = '/static/'
    # STATICFILES_DIR = [
    #     os.path.join(BASE_DIR, 'static')
    # ]
    # STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

    return render(request, template_name='index.html')
