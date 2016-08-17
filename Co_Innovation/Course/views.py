#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from SystemArticle.models import Article, Column
from Course.models import Course
from django.core.paginator import *
import datetime
# Create your views here.

def index(request):
    request.session['current_path'] = request.path
    try:
        course_list = Course.objects.all()
        paginator = Paginator(course_list, 7)
        try:
            page = request.GET.get('page', 1)
            page_course = paginator.page(page)
        except PageNotAnInteger:
            page_course = paginator.page(1)
        except EmptyPage:
            page_course = paginator.page(paginator.num_pages)
        info = {'page_course':page_course, 'paginator':paginator}
        return render(request, 'Course/index.html', info)
    except:
        return HttpResponse('error')

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
        return render(request, 'Course/course_detail.html', info)
    except:
        return HttpResponse('error')

@csrf_exempt
def preview(request):
    return HttpResponse('预览')
