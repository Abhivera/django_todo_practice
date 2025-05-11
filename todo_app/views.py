from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Todo
from .forms import TodoForm

# List all todos
class TodoListView(ListView):
    model = Todo
    template_name = 'todo_app/todo_list.html'
    context_object_name = 'todos'
    ordering = ['-created_at']

# View a single todo
class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todo_app/todo_detail.html'

# Create a new todo
class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo_app/todo_form.html'
    success_url = reverse_lazy('todo-list')

# Update a todo
class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo_app/todo_form.html'
    success_url = reverse_lazy('todo-list')

# Delete a todo
class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todo_app/todo_confirm_delete.html'
    success_url = reverse_lazy('todo-list')

# Toggle completion status
def toggle_complete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo-list')