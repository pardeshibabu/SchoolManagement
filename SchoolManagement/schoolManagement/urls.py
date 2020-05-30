"""schoolManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from .views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/profile/', ProfilePage.as_view(template_name = 'users/profile.html'), name="profile_page"),
    # path('users/', include('users.urls')),
    path('', index, name="index"),
    path('templates/index.html', index, name="index"),
    path('templates/about.html', index, name="index"),
    path('templates/blog.html', index, name="blog"),
    path('templates/blog-single.html', index, name="blog-single"),
    path('templates/contact.html', index, name="contact"),
    path('templates/courses.html', index, name="courses"),
    path('templates/pricing.html', index, name="pricing"),
    path('templates/teacher.html', index, name="teacher"),
    # path('users/', include('django.contrib.auth.urls')),
    # path('accounts/', include('officeaccounts.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),

                      # For django versions before 2.0:
                      # url(r'^__debug__/', include(debug_toolbar.urls)),

                  ] + urlpatterns
