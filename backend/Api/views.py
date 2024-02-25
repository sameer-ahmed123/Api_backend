from django.http import JsonResponse
from django.shortcuts import render
from Api.models import Employees
from rest_framework import generics
from Api.serializers import EmployeeSerializer

from rest_framework.permissions import DjangoModelPermissions
from Api.permissions import IsStaffEmployeePersmissions

# below two are required for a django rest framework  "VIEW"
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import permissions, authentication
# Create your views here.


class ShowEmployeeAPIView(generics.ListCreateAPIView):
    queryset = Employees.objects.all()
    authentication_classes = [authentication.SessionAuthentication]
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAdminUser, IsStaffEmployeePersmissions]


class ProductListCreateAPIView(generics.ListCreateAPIView):
    # queryset = Products.objects.all()
    # authentication_classes = [authentication.SessionAuthentication]
    # serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPersmissions]

    def perform_create(self, serializer):
        # serializer.save(user = self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get('Title')
        content = serializer.validated_data.get('content')

        if content is None:
            content = title

        serializer.save(content=content)


def hello_world(request):
    data = {"message": "hello world!"}
    return JsonResponse(data)


@api_view(['GET'])
def Empl_show(request):
    instance = Employees.objects.all()

    if instance:
        data = EmployeeSerializer(
            instance, context={'request': request}, many=True).data
    else:
        data = "fuck off no data here"

    return Response(data)


class EmployeeDelete(generics.DestroyAPIView):
    lookup_field = 'pk'
    serializer_class = EmployeeSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser, IsStaffEmployeePersmissions]
    queryset = Employees.objects.all()

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
