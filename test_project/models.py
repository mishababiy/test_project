# coding: utf-8

from django.db import models
from django.db.models.signals import post_init

class Lesson(models.Model):
    headline = models.CharField(max_length=100)
    source = models.CharField(max_length=200)
    created = models.DateTimeField()

class Comment(models.Model):
    text = models.TextField()
    created = models.DateTimeField()
    student = models.CharField(max_length=100)
    lesson = models.ForeignKey(Lesson)

    class Meta:
        ordering = ('-created',)



def extraInitForLesson(**kwargs):
   instance = kwargs.get('instance')
   if len(instance.source) == 11:
        pass
   else:
       instance.source = instance.source[31:43]

post_init.connect(extraInitForLesson, Lesson)



