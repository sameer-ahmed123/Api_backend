from rest_framework import serializers
from App.models import Task


class TaskSerializer(serializers.ModelSerializer):
    state = serializers.SerializerMethodField()

    def get_state(self, obj):
        return obj.Retrive_state()

    class Meta:
        model = Task
        fields = [
            'id',
            'Task_title',
            'Slug',
            'Content',
            'state',
        ]
