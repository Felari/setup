from django.shortcuts import render
from .models import Todo
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import View
from django.shortcuts import get_object_or_404, redirect
from datetime import date

from django.urls import reverse_lazy

# Create your views here.

class TodoListView(ListView):
    model = Todo

class TodoCreateView (CreateView):
    model = Todo
    fields = ["title", "deadline", "pessoa_responsavel"]
    success_url = reverse_lazy("todo_list")

class TodoUpdateView (UpdateView):
    model = Todo
    fields = ["title", "deadline", "pessoa_responsavel"]
    success_url = reverse_lazy("todo_list")

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")

class TodoCompleteView(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.finish_at = date.today()
        todo.save()
        return redirect("todo_list")
    