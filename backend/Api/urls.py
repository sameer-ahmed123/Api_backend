
from django.urls import path
from Api.views import hello_world, Empl_show, EmployeeDelete, ShowEmployeeAPIView

urlpatterns = [
    path("hello", hello_world),
    path("empl", Empl_show),
    path("list", ShowEmployeeAPIView.as_view()),
    path("delete/<int:pk>/", EmployeeDelete.as_view(), name="delete_emp"),
]
