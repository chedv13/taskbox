from test_plus.test import TestCase
from ..models import Task


class TestTask(TestCase):
    def setUp(self):
        self.user = self.make_user()
        self.task = Task.objects.create(user=self.user, text='test text')

    def test_default_done(self):
        self.assertEqual(self.task.done, False)
