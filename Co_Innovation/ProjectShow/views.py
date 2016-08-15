from django.shortcuts import render
from django.http import HttpResponse
from ProjectShow.models import Project, Task
from User.models import User
from django.core.paginator import *

# Create your views here.
def index(request):
    request.session['current_path'] = request.path
    try:
        project_list = Project.objects.all()
        paginator = Paginator(project_list, 8)
        page = request.GET.get('page', 1)
        try:
            page_project = paginator.page(page)
        except PageNotAnInteger:
            page_project = paginator.page(1)
        except EmptyPage:
            page_project = paginator.page(paginator.num_pages)
        info = {'page_project':page_project, 'paginator':paginator}
        return render(request, 'ProjectShow/index.html', info)
    except:
        return HttpResponse('error')


def project_manage(request):
    request.session['current_path'] = request.path
    if request.session['root'] & 1 :
        project_list = Project.objects.all()
    else:
        try:
            principal_name = request.session['user_name']
            principal = User.objects.get(user_name = principal_name)
            project_list = Project.objects.filter(principal = principal)
        except:
            return HttpResponse('Error')
    info = {'project_list':project_list}
    return render(request, 'ProjectShow/project_manage.html', info)

def project_detail(request, project_id):
    request.session['current_path'] = request.path
    try:
        project = Project.objects.get(id = project_id)
        project.reading_quantity += 1;
        project.save()
        task_list = project.task_set.all()
        info = {'project': project, 'task_list':task_list}
        return render(request, 'ProjectShow/project_detail.html', info)
    except:
        return HttpResponse("error")
