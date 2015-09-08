from django.views.generic import edit, DetailView, ListView
from braces.views import LoginRequiredMixin, UserFormKwargsMixin
from .models import Task, TaskStatus
from .forms import TaskForm
from django.forms.models import modelform_factory
from django.forms import TypedChoiceField


class TaskCreateView(LoginRequiredMixin, edit.CreateView):
    form_class = TaskForm
    template_name = 'tasks/new.html'
    success_url = '/tasks'

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super(TaskCreateView, self).form_valid(form)


class TaskUpdateView(LoginRequiredMixin, edit.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/edit.html'
    success_url = '/tasks'

    def get_form_kwargs(self):
        kwargs = super(TaskUpdateView, self).get_form_kwargs()

        kwargs.update({'additional_fields': ['status']})

        return kwargs


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
