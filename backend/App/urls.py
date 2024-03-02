from django.urls import path
from App.views import Index, Detail_task, Delete_task, Update_task
urlpatterns = [
    path("", Index, name="index"),
    path("task/<slug:slug>/", Detail_task, name="detail"),
    path("task/update/<slug:slug>/", Update_task, name="update"),
    path("task/delete/<slug:slug>/", Delete_task, name="delete"),
]
