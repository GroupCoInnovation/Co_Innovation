#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from SystemArticle.models import Column, Article
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from django.core.paginator import *
from SystemArticle.upload_proc import *
import django.utils.timezone
import datetime
# Create your views here.

def index(request):
    request.session['current_path'] = request.path
    column_list = Column.objects.filter(category = 'SC') # 所有的系统栏目
    article_list = Article.objects.filter(category = 'SA') # 所有的系统文章
    hotest_list = article_list.order_by('-reading_quantity') #按阅读量排序
    hotest_list = hotest_list[0:6]
    paginator = Paginator(article_list, 7) #一页七篇文章
    page = request.GET.get('page', 1)  #url后如果没有查询集 ?page=.., 则page=1
    try:
        page_article = paginator.page(page)
    except PageNotAnInteger:  #  page如果不是整合, 取page=1
        page_article = paginator(1)
    except EmptyPage: # 没有此页
        page_article = paginator(paginator.num_page) #取最后一页

    info = {'column_list':column_list, 'page_article':page_article, 'paginator':paginator, 'hotest_list': hotest_list}
    return render(request, 'SystemArticle/index.html', info)

@csrf_exempt
def column(request, column_id):
    request.session['current_path'] = request.path
    column_list = Column.objects.filter(category = 'SC') # 所有的系统栏目
    column = Column.objects.get(pk = column_id)

    if column == False:
        return HttpResponse('information Error')
    else :
        article_list = column.article_set.all()
        hotest_list = article_list.order_by('-reading_quantity')  # 按阅读量排序
        hotest_list = hotest_list[0:6]
        paginator = Paginator(article_list, 7)
        page = request.GET.get('page', 1)
        try:
            page_article = paginator.page(page)
        except PageNotAnInteger:
            page_article = paginator.page(1)
        except EmptyPage:
            page_article = paginator.page(paginator.num_pages)
        info = {'column_list':column_list, 'column':column, 'page_article':page_article, 'paginator':paginator, 'hotest_list': hotest_list}
        return render(request, 'SystemArticle/column.html', info)


def top(request, article_id):
    try:
        article = Article.objects.get(id = article_id)
        article.top = True
        article.top_time = datetime.datetime.now()
        column_id = article.column.id
        article.save()
        return HttpResponseRedirect(request.session['current_path'])
    except:
        return HttpResponse('server error')


def untop(request, article_id):
    try:
        article = Article.objects.get(id = article_id)
        article.top = False
        article.save()
        return HttpResponseRedirect(request.session['current_path'])
    except:
        return HttpResponse('server error')


def delete_article(request, article_id):
    try:
        article = Article.objects.get(id = article_id)
        column_id = article.column.id
        article.delete() # delete the object
        return HttpResponseRedirect(reverse('SystemArticle_column', args = [column_id]))
    except:
        return  HttpResponse('server error')


def article(request, article_id):
    request.session['current_path'] = request.path
    article = Article.objects.get(pk = article_id)
    article_list = Article.objects.filter(category='SA')  # 所有的系统文章
    hotest_list = article_list.order_by('-reading_quantity')  # 按阅读量排序
    hotest_list = hotest_list[0:6]
    if article == False:
        return HttpResponse('information error')
    else :
        article.reading_quantity += 1
        article.save()
        info = {'article':article, 'hotest_list': hotest_list}
        return render(request, 'SystemArticle/article.html', info)


@csrf_exempt
def write_article(request):
    column_list = Column.objects.filter(category = 'SC')
    info = {'column_list':column_list}
    if request.method == 'GET':
        return render(request, 'SystemArticle/write_article.html', info)
    else: # POST
        cover = request.FILES.get('cover_image', False)
        column_name = request.POST['column_name']
        summary = request.POST['summary']
        content = request.POST['content']
        title = request.POST['title']
        article = Article()
        if cover:
            article.cover = cover
        article.category = 'SA' # 系统文章
        article.column = Column.objects.get(column_name = column_name)
        article.summary, article.title, article.content =summary,  title, content
        article.top_time = datetime.datetime.now()
        article.save()
        return HttpResponseRedirect(reverse('SystemArticle_index'))


@csrf_exempt
def edit_article(request, article_id):
    try:
        article = Article.objects.get(id = article_id)
        info = {'article':article}
    except:
        return HttpResponse('server error')
    if request.method == 'GET':
        return render(request, 'SystemArticle/edit_article.html', info)
    else :
        cover = request.FILES.get('cover_image', False)
        if cover:
            article.cover = cover
        article.title = request.POST['title']
        article.content = request.POST['content']
        article.save()
        return HttpResponseRedirect(reverse('SystemArticle_index'))


@csrf_exempt
def preview(request):
    cover = request.FILES['cover_image']
    column_name = request.POST['column_name']
    content = request.POST['content']
    title = request.POST['title']
    summary = request.POST['summary']
    article = Article()
    article.column = Column.objects.get(column_name=column_name)
    article.cover,article.title, article.content = cover, title, content
    article.top_time = datetime.datetime.now()
    article.pub_date = datetime.datetime.now()
    article.save()
    article.delete()
    info = {'article': article}
    return render(request, 'SystemArticle/preview.html', info)


def show_upload_file(request):
    return render(request, 'SystemArticle/upload_file.html')


@csrf_exempt
def upload_file(request):


    files = request.FILES['fileData']
    today = datetime.datetime.today()
    file_dir = settings.MEDIA_ROOT + '/%d/%d/%d/' % (today.year, today.month, today.day)
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)

    # filename = file[12:]
    file_path = file_dir + files.name

    upload_url = settings.MEDIA_URL + '%d/%d/%d/'%(today.year, today.month, today.day) + files.name
    try:
        open(file_path, 'wb+').write(files.read())  # 上传文件
        return HttpResponse(upload_url)
    except:
        return HttpResponse('error')