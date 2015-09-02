from django.views.generic import edit, DetailView, ListView
from .models import Task
from .forms import TaskForm


class TaskCreateView(edit.CreateView):
    form_class = TaskForm
    template_name = 'tasks/new.html'
    success_url = '/tasks'


class TaskUpdateView(edit.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/edit.html'
    success_url = '/tasks'


class TaskDeleteView(edit.DeleteView):
    model = Task
    success_url = '/tasks'


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/index.html'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/show.html'
