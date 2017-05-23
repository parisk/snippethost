from django.contrib import admin

from snippets import models


@admin.register(models.Snippet)
class SnippetAdmin(admin.ModelAdmin):
    pass
