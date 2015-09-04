# -*- coding:utf-8 -*-

from django.forms import ModelForm, Textarea
from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('text', 'done')
        widgets = {
            'text': Textarea(attrs={'cols': 80, 'rows': 10})
        }
        error_messages = {
            'text': {
                'required': 'Пожалуйста, укажите текст задачи'
            }
        }
