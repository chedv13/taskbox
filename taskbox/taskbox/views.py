from django.views.generic import edit
from .models import Task
from .forms import TaskForm


class CreateTaskView(edit.CreateView):
    form_class = TaskForm
    template_name = 'tasks/new.html'


class UpdateTaskView(edit.UpdateView):
    model = Task


class DeleteTaskView(edit.DeleteView):
    model = Task
    success_url = '/tasks'
