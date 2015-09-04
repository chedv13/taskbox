from django.test import TestCase, RequestFactory
from taskbox.taskbox.tests.factories import *
from django.core.urlresolvers import reverse

import django

django.setup()


class BaseUserTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.factory = RequestFactory()
        self.client.login(username=self.user.username, password='adm1n')


class TestTaskCreateView(BaseUserTestCase):
    def test_create_task_with_text(self):
        self.assertEqual(Task.objects.count(), 0)
        self.client.post(reverse('taskbox:create_task'), {'text': 'test text'})
        self.assertEqual(Task.objects.count(), 1)

    def test_create_task_without_text(self):
        self.assertEqual(Task.objects.count(), 0)
        self.client.post(reverse('taskbox:create_task'), {'text': ''})
        self.assertEqual(Task.objects.count(), 0)


class TestTaskUpdateView(BaseUserTestCase):
    def test_update_task(self):
        task = TaskFactory(user=self.user)

        self.assertEqual(Task.objects.count(), 1)
        self.client.post(reverse('taskbox:update_task', args=(task.id,)), {'text': 'test'})
        self.assertEqual(Task.objects.first().text, 'test')


class TestTaskDeleteView(BaseUserTestCase):
    def test_delete_task(self):
        task = TaskFactory(user=self.user)

        self.assertEqual(Task.objects.count(), 1)
        self.client.delete(reverse('taskbox:delete_task', args=(task.id,)))
        self.assertEqual(Task.objects.count(), 0)


class TestTaskDetailView(BaseUserTestCase):
    def test_detail_view(self):
        task = TaskFactory(user=self.user)

        response = self.client.get('/tasks/%d' % (task.id))
        self.assertEqual(response.status_code, 200)


class TestTaskListView(BaseUserTestCase):
    def test_index_view_without_tasks(self):
        response = self.client.get('/tasks')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Tasks not found")
        self.assertQuerysetEqual(response.context['task_list'], [])

    def test_index_view_wth_tasks(self):
        TaskFactory(user=self.user)

        response = self.client.get('/tasks')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['task_list'].count(), 1)
