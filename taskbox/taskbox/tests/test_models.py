from django.test import TestCase
from taskbox.taskbox.tests.factories import *
from taskbox.taskbox.models import TaskStatus
from django.db.models import signals
# from mock import MagicMock
# from mock import patch
import mock


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

        # def test_mass_mail_sending_for_done_tasks(self):
        #     with mock.patch('taskbox.taskbox.models.send_mass_mail_for_done_tasks') as mocked_handler:
        #         signals.post_save.connect(mocked_handler, sender=Task, dispatch_uid='test_cache_mocked_handler')
        #     self.assertEqual(mocked_handler.call_count, 1)
