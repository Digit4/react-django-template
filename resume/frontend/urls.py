from django.urls import path, url
from views import index

urlpatterns = [
    path('', index),
]
