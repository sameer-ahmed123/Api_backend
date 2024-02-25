from rest_framework import serializers
from Api.models import Employees


class EmployeeSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Employees
        fields = [
            'id',
            'name',
            'designation',
            'salary',
            'image',
        ]
