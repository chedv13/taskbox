# -*- coding:utf-8 -*-

from django.db import models
from taskbox.users.models import User
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail


class Task(models.Model):
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('done', 'Done')
    )

    text = models.TextField(default='')
    user = models.ForeignKey(User)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='open')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __init__(self, *args, **kwargs):
        super(Task, self).__init__(*args, **kwargs)
        self.prev_status = self.status

    def clean(self):
        if self.status == 'open' and self.prev_status == 'in_progress':
            raise ValidationError('Статус In Progress не может перейти в Open')

    def status_verbose(self):
        return dict(Task.STATUS_CHOICES)[self.status]


@receiver(post_save, sender=Task, dispatch_uid='models.send_mass_mail_for_done_tasks')
def send_mass_mail_for_done_tasks(instance, **kwargs):
    if instance.status == 'open':
        user_email = instance.user.email
        emails = map(lambda user: str(user.email), User.objects.exclude(email=user_email))

        send_mail('Closing tasks', '%s closed task #%d.' % (user_email, instance.id), 'taskboxdev@yandex.ru',
                  emails)
