from django.views.generic import edit, DetailView, ListView
from braces.views import LoginRequiredMixin
from .models import Task
from .forms import TaskForm


class TaskCreateView(LoginRequiredMixin, edit.CreateView):
    form_class = TaskForm
    template_name = 'tasks/new.html'
    success_url = '/tasks'


class TaskUpdateView(LoginRequiredMixin, edit.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/edit.html'
    success_url = '/tasks'


class TaskDeleteView(LoginRequiredMixin, edit.DeleteView):
    model = Task
    success_url = '/tasks'


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/index.html'

    def get_queryset(self):
        tasks = Task.objects.filter(user_id=self.request.user.id)

        return tasks


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/show.html'
