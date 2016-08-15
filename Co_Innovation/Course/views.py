#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from SystemArticle.models import Article, Column
import datetime
# Create your views here.

def index(request):
    # return render(request, 'Course/index.html')
    # return HttpResponse('Course home')
    course_list = Article.objects.filter(category = 'CA')
    info = {'course_list':course_list}
    request.session['current_path'] = request.path
    return render(request, 'Course/index.html', info)

@csrf_exempt
def write_article(request):
    column_list = Column.objects.filter(category = 'CC')
    info = {'column_list':column_list}
    if request.method == 'GET':
        return render(request, 'Course/write_article.html', info)
    else: # POST
        cover = request.FILES.get('cover_image', False)
        column_name = request.POST['column_name']
        summary = request.POST['summary']
        content = request.POST['content']
        title = request.POST['title']
        article = Article()
        if cover:
            article.cover = cover
        article.category = 'CA' # 系统文章
        article.column = Column.objects.get(column_name = column_name)
        article.summary, article.title, article.content =summary,  title, content
        article.top_time = datetime.datetime.now()
        article.save()
        return HttpResponseRedirect(reverse('Course_index'))

@csrf_exempt
def preview(request):
    return HttpResponse('预览')
