import random
from django.shortcuts import render
from App.models import Task, Status
from rest_framework import generics
from Api.serializers import TaskSerializer
from django.shortcuts import get_object_or_404

from rest_framework.permissions import DjangoModelPermissions
from Api.permissions import IsStaffEmployeePersmissions

# below two are required for a django rest framework  "VIEW"
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import permissions, authentication
# Create your views here.


# class ShowEmployeeAPIView(generics.ListCreateAPIView):
#     queryset = Employees.objects.all()
#     authentication_classes = [authentication.SessionAuthentication]
#     serializer_class = EmployeeSerializer
#     permission_classes = [permissions.IsAdminUser, IsStaffEmployeePersmissions]


# @api_view(['GET'])
# def Empl_show(request):
#     instance = Employees.objects.all()

#     if instance:
#         data = EmployeeSerializer(
#             instance, context={'request': request}, many=True).data
#     else:
#         data = "fuck off no data here"

#     return Response(data)


# class EmployeeDelete(generics.DestroyAPIView):
#     lookup_field = 'pk'
#     serializer_class = EmployeeSerializer
#     authentication_classes = [authentication.SessionAuthentication]
#     permission_classes = [permissions.IsAdminUser, IsStaffEmployeePersmissions]
#     queryset = Employees.objects.all()

#     def perform_destroy(self, instance):
#         super().perform_destroy(instance)

@api_view(["POST"])
def Create_task_api(request):
    Task_instance = TaskSerializer(data=request.data)
    recived_status_id = request.data.get("Status")

    if Task_instance.is_valid():
        # get Status
        try:
            status = Status.objects.get(id=recived_status_id)
        except Status.DoesNotExist:
            return Response({"Message": "Invalid Status ID"})

        if Task_instance.is_valid():
            # .save(commit=False) ====> .save("model_field"= "some data")  in drf
            Task_instance.save(status=status)
            return Response(Task_instance.data)

    return Response({"Message": "Invalid format!"})


@api_view(["GET"])
def List_Task_api(request):
    instance = Task.objects.all()
    if instance:
        data = TaskSerializer(instance, many=True).data
    else:
        data = {"Message": "Sorry, no Tasks available !"}
    return Response(data)


@api_view(["GET"])
def Detail_Task_api(request, slug):
    task_instance = get_object_or_404(Task, Slug=slug)
    if task_instance:
        data = TaskSerializer(task_instance).data

    return Response(data)


@api_view(["DELETE"])
def Delete_Task_api(request, slug):
    task_instance = get_object_or_404(Task, Slug=slug)
    if task_instance:
        task_instance.delete()
        response_msg = {"alert": "Task has been Deleted."}
    return Response(response_msg)


@api_view(["POST"])
def Update_Task_api(request, slug):
    task_instance = get_object_or_404(Task, Slug=slug)
    updated_task = TaskSerializer(instance=task_instance, data=request.data)

    if updated_task.is_valid():
        # the data recived from the api_request  for status should be "Status"
        new_status_id = request.data.get("Status")
        try:
            new_status = Status.objects.get(id=new_status_id)
        except Status.DoesNotExist:
            return Response({"message": "Invalid status ID"})
        updated_task.instance.status = new_status
        updated_task.save()
        return Response(updated_task.data)

    return Response({"message": "Not found!"})
