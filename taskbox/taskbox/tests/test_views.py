from django.test import TestCase, RequestFactory
from taskbox.taskbox.views import *
from taskbox.taskbox.tests.factories import *
from django.test import Client
from django.core.urlresolvers import reverse

import django

django.setup()


class BaseUserTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.factory = RequestFactory()


class TestTaskDetailView(BaseUserTestCase):
    def test_detail_view(self):
        task = TaskFactory(user=self.user)
        self.client.login(username=task.user.username, password='adm1n')

        response = self.client.get('/tasks/%d' % (task.id))
        self.assertEqual(response.status_code, 200)


class TestTaskListView(BaseUserTestCase):
    def test_index_view_without_tasks(self):
        self.client.login(username=self.user.username, password='adm1n')

        response = self.client.get('/tasks')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Tasks not found")
        self.assertQuerysetEqual(response.context['task_list'], [])

    def test_index_view_wth_tasks(self):
        TaskFactory(user=self.user)
        self.client.login(username=self.user.username, password='adm1n')

        response = self.client.get('/tasks')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['task_list'].count(), 1)

#
# class TestTaskCreateView():
#     def test_create_task_with_text(self):
