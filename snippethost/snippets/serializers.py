from django.contrib.auth.models import User
from rest_framework import serializers

from snippets.models import Snippet


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', )


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'user', 'text' )
