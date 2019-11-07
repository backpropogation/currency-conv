from django.contrib import admin
from .models import Rate


@admin.register(Rate)
class AuthorAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
