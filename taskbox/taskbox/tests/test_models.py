from django.test import TestCase
from taskbox.taskbox.tests.factories import *


class TestTask(TestCase):
    def setUp(self):
        self.task = TaskFactory()

    def test_done_default(self):
        self.assertEqual(
            self.task.done,
            False
        )

    def test_text_default(self):
        self.assertEqual(
            self.task.text,
            ''
        )
