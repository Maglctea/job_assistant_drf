from django.urls import path

from landingapp.views import RegisterUser

urlpatterns = [
    path('', RegisterUser.as_view(), name='add-user'),
]
