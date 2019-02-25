from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note


class NoteRootSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'title', 'create_at')


class NoteSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True)
    desc = serializers.CharField(required=True)
    create_at = serializers.DateTimeField()
    users = serializers.PrimaryKeyRelatedField(
            many=False,
            queryset=User.objects.all()
        )

    def create(self, validated_data):
        return Note.objects.create(**validated_data)


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField()
    date_joined = serializers.DateTimeField()