from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from User.models import User
from django.core.urlresolvers import reverse
from SystemArticle.models import Article, Column
from ProjectShow.models import Project
from django.core.paginator import *



def home(request):
    request.session['current_path'] = request.path
    # info = {'is_log_in': True, 'request':request}
    # if request.session.get('user_name', False) == False:
    #     info['is_log_in'] = False
    course_list = Article.objects.filter(category = 'CA').order_by('-reading_quantity')[:8]
    SystemArticle_list = Article.objects.filter(category = 'SA')[:8]
    project_list = Project.objects.all().order_by('-reading_quantity')[:8]
    info = {'course_list':course_list, 'SystemArticle_list':SystemArticle_list, 'project_list':project_list}
    return render(request, 'home/home.html', info)

# # by the GET method get the queryset option_url_name=.....
# def root_process(request):
#     option_url_name = request.GET.get('option_url_name', 'home')
#     return HttpResponseRedirect(reverse(option_url_name))    # go to the edit views such as writing


def personal_homepage(request):
    # if not request.session.user_name:
    #     return HttpResponse('Error')
    # try:
        user_name = request.session['user_name']
        user = User.objects.get(user_name = user_name)
        # user information, the project the principal of which is the user,and the member of which is the user
        # project_of_finished = Project.objects.filter(principal = user || )
        # project_of_member = Project.objects.filter( = )
        project_of_principal_finished_list = user.principal_project_set.exclude(status = 0);
        project_of_member_finished_list = user.member_project_set.exclude(status = 0);
        project_of_finished_list = project_of_principal_finished_list | project_of_member_finished_list

        project_of_principal_unfinished_list = user.principal_project_set.filter(status = 0);
        project_of_member_unfinished_list = user.member_project_set.filter(status = 0);
        project_of_unfinished_list = project_of_principal_unfinished_list | project_of_member_unfinished_list

        paginator_finished = Paginator(project_of_finished_list,4 )
        paginator_unfinished = Paginator(project_of_unfinished_list,4 )

        try:
            page_finished = request.GET.get('page', 1)
            # page_finished = request.GET.get('page', 1)
            project_of_finished_list = paginator_finished.page(page_finished)
            # project_of_unfinished_list = paginator.page(page)
        except PageNotAnInteger:
            project_of_finished_list = paginator_finished.page(1)
        except EmptyPage:
            project_of_finished_list = paginator_finished.page(paginator_finished.num_pages)

        try:
            page_unfinished = request.GET.get('page', 1)
            project_of_unfinished_list = paginator_unfinished.page(page_unfinished)
        except PageNotAnInteger:
            project_of_unfinished_list = paginator_unfinished.page(1)
        except EmptyPage:
            project_of_unfinished_list = paginator_unfinished.page(paginator_unfinished.num_pages)

        # info = {'page_course':page_course, 'paginator':paginator, 'column_list':column_list}

        info = {'user':user, 'project_of_finished_list':project_of_finished_list, 'project_of_unfinished_list':project_of_unfinished_list}
        info['paginator_finished'] = paginator_finished;
        info['paginator_unfinished'] = paginator_unfinished;

        return render(request, 'home/personal_homepage.html', info)
    # except:
        # return HttpResponse('error')


def fuzzy_search(request):
    # article_title, project_name,
    search_item = request.POST['search_item']
    article_list = Article.objects.filter(title__contains = search_item)
    project_list = Project.objects.filter(project_name__contains = search_item)
    # article_list = Article.objects.all();
    # project_list = Project.objects.all();
    info = {'article_list':article_list, 'project_list':project_list}
    return render(request, 'home/fuzzy_search.html', info)
