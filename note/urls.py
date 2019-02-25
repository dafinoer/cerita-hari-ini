from django.urls import path
from .views import NoteList, NoteCreateView, NoteDetailView
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns

# api/notes/

urlpatterns = [
    path('api/v1/stories/', NoteList.as_view(), name='story-note-list'),
    path('api/v1/core/notes', NoteCreateView.as_view(), name='note-create'),
    path('api/v1/core/notes/<int:pk>/', NoteDetailView.as_view(), name='note-detail')
]