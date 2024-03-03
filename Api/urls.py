
from django.urls import path
from Api.views import List_Task_api, Detail_Task_api, Delete_Task_api, Update_Task_api,Create_task_api

urlpatterns = [
    path("tasks", List_Task_api),
    path("task/create/",Create_task_api),
    path("task/<slug:slug>/", Detail_Task_api),
    path("task/<slug:slug>/delete/", Delete_Task_api),
    path("task/<slug:slug>/update/", Update_Task_api),
]
