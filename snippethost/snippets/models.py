from django.contrib.auth.models import User
from django.db import models


class Snippet(models.Model):
    user = models.ForeignKey(User)
    text = models.TextField()
