# -*- coding: utf-8 -*-

from django.test import TestCase
from taskbox.taskbox.forms import TaskForm


class TestTaskForm(TestCase):
    def test_task_form_with_empty_text(self):
        form_data = {'text': ''}
        form = TaskForm(data=form_data, fields=['text'])
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        self.assertEquals(form.errors['text'], [u"This field is required."])

    def test_task_form_with_text(self):
        form_data = {'text': 'test text'}
        form = TaskForm(data=form_data, fields=['text'])

        self.assertTrue(form.is_valid())
