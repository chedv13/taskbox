# -*- coding:utf-8 -*-

from django.forms import ModelForm, ChoiceField, CharField, Select
from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        exclude = ['user']
        error_messages = {
            'text': {
                'required': 'Пожалуйста, укажите текст задачи'
            }
        }

    # Господи, ну и трэш ...
    def __init__(self, *args, **kwargs):
        self.fields = kwargs.pop("fields", None)

        if self.fields:
            self._meta.fields = self.fields
            self.base_fields.clear()

            for field in self.fields:
                if field == "text":
                    self.base_fields[field] = CharField(label='Text')
                elif field == "status":
                    self.base_fields[field] = ChoiceField(widget=Select, choices=Task.STATUS_CHOICES)

        super(TaskForm, self).__init__(*args, **kwargs)
