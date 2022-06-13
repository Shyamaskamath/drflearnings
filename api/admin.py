from django.contrib import admin

# Register your models here.
from .models import Todolist

@admin.register(Todolist)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','create_at','update_at','completed']
