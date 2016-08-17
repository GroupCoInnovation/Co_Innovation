#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from SystemArticle.models import Article, Column
import datetime
from Course.models import Course
# Create your views here.

def index(request):
    # return render(request, 'Course/index.html')
    # return HttpResponse('Course home')
    course_list = Course.objects.all()
    info = {'course_list':course_list}
    request.session['current_path'] = request.path
    return render(request, 'Course/index.html', info)

@csrf_exempt
def write_course(request):
    column_list = Column.objects.filter(category = 'CC')
    info = {'column_list':column_list}
    if request.method == 'GET':
        return render(request, 'Course/write_course.html', info)
    else: # POST
        cover = request.FILES.get('cover_image', False)
        column_name = request.POST['column_name']
        title = request.POST['title']
        course_intro = request.POSR['course_intro']
        course = Course()
        if cover:
            course.cover = cover
        course.column = Column.objects.get(column_name = column_name)
        course.title, course.course_intro = title, course_intro
        course.time = datetime.datetime.now()
        course.save()
        return HttpResponseRedirect(reverse('Course_index'))

def course(request, course_id):
    try:
        course = Course.objects.get(pk = course_id)
        info = {'course':course}
        return render(request, 'Course/coursr_detail.html', info)
    except:
        return HttpResponse('error')

@csrf_exempt
def preview(request):
    return HttpResponse('预览')
