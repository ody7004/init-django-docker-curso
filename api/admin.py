from django.contrib import admin
from .models import Task, Comment



# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display=['id','title','priority','expired_at']
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass