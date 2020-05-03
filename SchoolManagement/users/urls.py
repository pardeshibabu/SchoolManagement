from django.urls import path
from .views import ProfilePage


app_name = "users"

urlpatterns = [
    path('accounts/profile/', ProfilePage.as_view(), name="profile_page"),
]
