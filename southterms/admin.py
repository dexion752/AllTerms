from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Sources)
class SourcesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'code', 'sum')
    search_fields = ('title', 'author', 'code')
    ordering = ['id', 'title']


# admin.site.register(Sources, SourcesAdmin)

# Register your models here.
