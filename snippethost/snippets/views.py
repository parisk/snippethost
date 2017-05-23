from django.contrib.auth.models import User
from rest_framework import viewsets

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from snippets.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    serializer_class = SnippetSerializer

    def get_queryset(self):
        user = User.objects.get(pk=self.kwargs.get('user_id'))
        return Snippet.objects.filter(user=user)
