from django.core import mail
from django.test import TestCase


class EmailTest(TestCase):
    def test_send_email(self):
        mail.send_mail('Subject here', 'Here is the message.',
                       'testbox@yandex.ru', ['chedv13@gmail.com'],
                       fail_silently=False)
        self.assertEquals(len(mail.outbox), 1)
        self.assertEquals(mail.outbox[0].subject, 'Subject here')
