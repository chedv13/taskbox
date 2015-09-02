# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'tasks/new$',
        view=views.CreateTaskView.as_view(),
        name='edit_task'
    ),
    url(
        regex=r'^tasks/(?P<pk>\d+)/edit$',
        view=views.UpdateTaskView.as_view(),
        name='update_task'
    ),
    url(
        regex=r'^tasks/(?P<pk>\d+)/delete$',
        view=views.DeleteTaskView.as_view(),
        name='delete_task'
    )
]
