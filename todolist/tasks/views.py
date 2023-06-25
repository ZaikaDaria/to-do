from .models import Todo, Tag
from .forms import TodoForm, TagForm

from django.shortcuts import redirect
from django.views import generic
from django.urls import reverse, reverse_lazy


class TodoListView(generic.ListView):
    model = Todo
    context_object_name = "todo_list"
    paginate_by = 7


class TodoCreateView(generic.CreateView):
    model = Todo
    form_class = TodoForm
    template_name = "tasks/todo_form.html"
    success_url = reverse_lazy("todo:todo-list")


class TodoUpdateView(generic.UpdateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy("todo:todo-list")


class TodoDeleteView(generic.DeleteView):
    model = Todo
    success_url = reverse_lazy("todo:todo-list")


class TodoUpdateStatusView(generic.View):

    def get(request, pk):
        task = Todo.objects.get(id=pk)
        task.is_complete = not task.is_complete
        task.save()
        return redirect("todo:todo-list")

    def post(request, pk):
        task = Todo.objects.get(id=pk)
        task.is_complete = request.POST.get("is_complete", not task.is_complete)
        task.save()
        return redirect("todo:todo-list")


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm

    def get_success_url(self):
        return reverse("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")
