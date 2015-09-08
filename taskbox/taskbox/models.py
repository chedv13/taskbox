# -*- coding:utf-8 -*-

from django.db import models
from taskbox.users.models import User
from django_enumfield import enum
from django.core.exceptions import ValidationError


class TaskStatus(enum.Enum):
    OPEN = 0
    IN_PROGRESS = 1
    DONE = 2

    labels = {
        OPEN: 'Open',
        IN_PROGRESS: 'In Progress',
        DONE: 'Done'
    }


class Task(models.Model):
    text = models.TextField(default='')
    user = models.ForeignKey(User)
    status = enum.EnumField(TaskStatus, default=TaskStatus.OPEN)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __init__(self, *args, **kwargs):
        super(Task, self).__init__(*args, **kwargs)
        self.prev_status = self.status

    def clean(self):
        if self.status == 0 and self.prev_status == 1:
            raise ValidationError('Статус In Progress не может перейти в Open')
