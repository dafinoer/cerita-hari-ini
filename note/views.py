from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializer import (
    UserSerializer,
    NoteSerializer,
    NoteRootSerializer
)
from .models import Note
# Create your views here.
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from rest_framework.pagination import LimitOffsetPagination


class MyPagination(LimitOffsetPagination):
    default_limit = 20


class NoteList(APIView):

    permission_classes = (IsAuthenticated,)
    # pagination_class = MyPagination

    def get(self, request, format=None):
        notes = Note.objects.all().order_by('-id')
        paginator = LimitOffsetPagination()
        result_page = paginator.paginate_queryset(notes, request)
        serializer = NoteRootSerializer(result_page, many=True)
        return Response(serializer.data)


class NoteCreateView(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoteDetailView(APIView):

    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Note.objects.get(pk=pk)
        except Note.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        id_note = self.get_object(pk)
        serializer = NoteSerializer(id_note)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        objects = self.get_object(pk)
        serializer = NoteSerializer(objects, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        note = self.get_object(pk)
        print(note)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)