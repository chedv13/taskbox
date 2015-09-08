from django.test import TestCase
from taskbox.taskbox.tests.factories import *
from taskbox.taskbox.models import TaskStatus


class TestTask(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.task = TaskFactory(user=self.user)

    def test_text_default_is_empty_string(self):
        self.assertEqual(
            self.task.text,
            ''
        )

    def test_status_default_is_open(self):
        self.assertEqual(
            self.task.status,
            TaskStatus.OPEN
        )
