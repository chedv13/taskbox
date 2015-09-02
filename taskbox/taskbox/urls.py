# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'tasks/new$',
        view=views.TaskCreateView.as_view(),
        name='create_task'
    ),
    url(
        regex=r'^tasks/(?P<pk>\d+)/edit$',
        view=views.TaskUpdateView.as_view(),
        name='update_task'
    ),
    url(
        regex=r'^tasks/(?P<pk>\d+)/delete$',
        view=views.TaskDeleteView.as_view(),
        name='delete_task'
    ),
    url(
        regex=r'^tasks/(?P<pk>\d+)$',
        view=views.TaskDetailView.as_view(),
        name='show_task'
    ),
    url(
        regex=r'^tasks$',
        view=views.TaskListView.as_view(),
        name='show_tasks'
    )
]
