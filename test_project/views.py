# -*- coding: utf-8 -*- 

from django.contrib.auth.models import User, AnonymousUser
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import simplejson
from forms import CommentForm
from django.shortcuts import render
from django.contrib import auth
from models import Lesson, Comment
from django.contrib.auth.decorators import login_required
import datetime

def index(request):
    if request.user.is_authenticated():
        lessons = Lesson.objects.all()
        return render(request, 'index.html',{'lessons':lessons})
    else:
        about_lesson = Lesson.objects.get(id=1)
        print about_lesson
        print about_lesson.id
        print about_lesson.source
        return render(request, 'index.html',{'lesson':about_lesson})

@login_required
def view_lesson(request,id_lesson):

    lesson = Lesson.objects.get(id=id_lesson)
    comments = Comment.objects.filter(lesson=id_lesson)
    comment_form = CommentForm()
    return render(request, 'lesson.html',{'lesson':lesson, 'comments':comments,
                                          'comment_form':comment_form})

def ajax_comment(request,id_lesson):

    text = request.REQUEST['question']
    comment = Comment(text=text, student=request.user.email, created=datetime.datetime.now())
    lesson = Lesson.objects.get(id=id_lesson)
    lesson.comment_set.add(comment)
    result = {'comment':comment.text, 'student':comment.student}
    json = simplejson.dumps(result)
    return HttpResponse(json, mimetype='application/json')

