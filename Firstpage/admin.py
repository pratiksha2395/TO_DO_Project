from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    randomly_fields=('created',)
admin.site.register(Todo, TodoAdmin)
