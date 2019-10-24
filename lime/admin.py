from django.contrib import admin
from .models import Message

# Register your models here.
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'created', 'updated','content','is_public')
    list_filter = ('author', 'created',)
    search_fields = ('category', 'content')
    date_hierarchy = 'created'
    ordering = ('-updated',)
