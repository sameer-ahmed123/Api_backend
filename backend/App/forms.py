from django.forms import ModelForm
from App.models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            'Task_title',
            'Slug',
            'Content',
            'status'
        ]
