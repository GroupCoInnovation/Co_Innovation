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
from Course.form import DateTimeForm
# Create your views here.

def index(request):
    request.session['current_path'] = request.path
    column_list = Column.objects.filter(category = 'CC') # 所有的课程栏目
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
        info = {'page_course':page_course, 'paginator':paginator, 'column_list':column_list}
        return render(request, 'Course/index.html', info)
    except:
        return HttpResponse('error')

@csrf_exempt
def column(request, column_id):
    request.session['current_path'] = request.path
    column_list = Column.objects.filter(category = 'CC') # 所有的课程栏目
    column = Column.objects.get(pk = column_id)

    if column == False:
        return HttpResponse('information Error')
    else :
        course_list = column.course_set.all()
        hotest_list = course_list.order_by('-reading_quantity')  # 按阅读量排序
        hotest_list = hotest_list[0:6]
        paginator = Paginator(course_list, 7)
        page = request.GET.get('page', 1)
        try:
            page_course = paginator.page(page)
        except PageNotAnInteger:
            page_course = paginator.page(1)
        except EmptyPage:
            page_course = paginator.page(paginator.num_pages)
        info = {'column_list':column_list, 'column':column, 'page_course':page_course, 'paginator':paginator, 'hotest_list': hotest_list}
        return render(request, 'Course/column.html', info)


@csrf_exempt
def write_course(request):
    column_list = Column.objects.filter(category = 'CC')
    info = {'column_list':column_list}
    if request.method == 'GET':
        # form = DateTimeForm();
        # info['form'] = form;
        return render(request, 'Course/write_course.html', info)
    else: # POST
        cover = request.FILES.get('cover_image', False)
        column_name = request.POST['column_name']
        title = request.POST['title']
        summary = request.POST['summary']
        content = request.POST['content']
        speaker = request.POST['speaker']
        place = request.POST['place']
        course = Course()
        if cover:
            course.cover = cover
        course.column = Column.objects.get(column_name = column_name)
        course.title, course.summary, course.content, course.speaker, course.place  = title, summary, content,speaker, place
        course.time = datetime.datetime.now()
        course.save()
        return HttpResponseRedirect(reverse('Course_index'))

def course(request, course_id):
    try:
        course = Course.objects.get(pk = course_id)
        course.reading_quantity += 1
        course.save()
        hotest_list = Course.objects.all().order_by('-reading_quantity')[0:6]
        info = {'course':course, 'hotest_list':hotest_list}
        return render(request, 'Course/course_detail.html', info)
    except:
        return HttpResponse('error')

@csrf_exempt
def preview(request):
    cover = request.FILES['cover_image']
    column_name = request.POST['column_name']
    title = request.POST['title']
    summary = request.POST['summary']
    content = request.POST['content']
    speaker = request.POST['speaker']
    place = request.POST['place']
    # content = request.POST['content']
    # title = request.POST['title']
    # summary = request.POST['summary']
    course = Course()
    course.column = Column.objects.get(column_name=column_name)
    course.cover,course.title, course.content = cover, title, content
    course.save()
    course.delete()
    info = {'course': course}
    return render(request, 'Course/preview.html', info)
    # return HttpResponse('预览')


@csrf_exempt
def like(request, course_id):
    course = Course.objects.get(pk = course_id)
    course.like += 1
    course.save()
    return HttpResponseRedirect(reverse('Course_course', args=[course.id]))
    # return HttpResponse('hjbununiu')
    # return HttpResponse(str(course.like))
