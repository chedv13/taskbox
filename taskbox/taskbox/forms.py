# -*- coding:utf-8 -*-

from django.forms import ModelForm, Textarea, TypedChoiceField
from .models import Task, TaskStatus


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['text']
        widgets = {
            'text': Textarea(attrs={'cols': 80, 'rows': 10})
        }
        error_messages = {
            'text': {
                'required': 'Пожалуйста, укажите текст задачи'
            }
        }

    def __init__(self, *args, **kwargs):
        self.additional_fields = kwargs.pop("additional_fields", None)

        if self.additional_fields:
            for field in self.additional_fields:
                self._meta.fields.append(field)
                self.base_fields[field] = TypedChoiceField(choices=TaskStatus.choices(), coerce=int)

        super(TaskForm, self).__init__(*args, **kwargs)
