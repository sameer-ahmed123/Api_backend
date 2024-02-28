from django.urls import path
from App.views import Index
urlpatterns = [
    path("",Index)
]