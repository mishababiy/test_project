# coding: utf-8

from django.contrib import admin
from models import Lesson, Comment


class LessonAdmin(admin.ModelAdmin):
    list_display = ['headline', 'source']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['student', 'created']

admin.site.register(Lesson, LessonAdmin)
admin.site.register(Comment, CommentAdmin)

