from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoListView.as_view(), name='todo-list'),
    path('todo/<int:pk>/', views.TodoDetailView.as_view(), name='todo-detail'),
    path('todo/new/', views.TodoCreateView.as_view(), name='todo-create'),
    path('todo/<int:pk>/update/', views.TodoUpdateView.as_view(), name='todo-update'),
    path('todo/<int:pk>/delete/', views.TodoDeleteView.as_view(), name='todo-delete'),
    path('todo/<int:pk>/toggle/', views.toggle_complete, name='todo-toggle'),
]