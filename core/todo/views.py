# # Create your models here.
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.shortcuts import redirect
# from django.urls import reverse_lazy
# from django.views import View
# from django.views.generic import CreateView, DeleteView, ListView, UpdateView
# from todo.forms import TaskForm
# from todo.models import Task



# class TaskListView(LoginRequiredMixin, ListView):
#     queryset = Task.objects.all()
#     context_object_name = 'tasks'
#     paginate_by = 2
#     ordering = '-id'


# class TaskCreateView(LoginRequiredMixin, CreateView):
#     model = Task
#     form_class = TaskForm
#     success_url = reverse_lazy('todo:task-list')

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)


# class TaskEditView(LoginRequiredMixin, UpdateView):
#     model = Task
#     form_class = TaskForm
#     success_url = reverse_lazy('todo:task-list')


# class TaskDeleteView(LoginRequiredMixin, DeleteView):
#     model = Task
#     success_url = reverse_lazy('todo:task-list')

#     def get(self, request, *args, **kwargs):
#         return self.delete(request, *args, **kwargs)


# class TaskComplete(LoginRequiredMixin, View):
#     model = Task
#     success_url = reverse_lazy("todo:task-list")

#     def get(self, request, *args, **kwargs):
#         object = Task.objects.get(id=kwargs.get("pk"))
#         object.status = True
#         object.save()
#         return redirect(self.success_url)

