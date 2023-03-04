from django import forms
from task.models import TaskList


class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ['task', 'done']
