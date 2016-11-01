from django.shortcuts import render
from django.http import HttpResponse
from ProjectShow.models import Project, Task
from User.models import User
from django.core.paginator import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
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
        project.reading_quantity += 1
        project.save()
        task_list = project.task_set.all()
        info = {'project': project, 'task_list':task_list}
        return render(request, 'ProjectShow/project_detail.html', info)
    except:
        return HttpResponse("error")


def project_manage_princ(request, project_id):
    request.session['current_path'] = request.path
    project = Project.objects.get(id=project_id)
    members = project.members.all()
    member_info_list = dict()
    for member_info in members:
        try:
            role = member_info.worker.get(task_name='Moren').role
        except:
            role = 1
        member_info_list[member_info] = role
    info = {'project': project, 'member_info_list':member_info_list}
    # d
    return render(request, 'ProjectShow/ProjectManage_leader.html', info)


@csrf_exempt
def change_project_name_and_intro(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
        project.project_name = request.POST['title']
        project.project_intro = request.POST['intro']
        project.save()
        return HttpResponse('ok')
    except:
        return HttpResponse('error')


@csrf_exempt
def end_project(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
        project.status = 1
        project.save()
        return HttpResponse('ok')
    except:
        return HttpResponse('error')


@csrf_exempt
def add_member(request, project_id):

    try:
        a = request.POST.get('ID_input3','Preke')
        project = Project.objects.get(id=project_id)
        temp_user = User.objects.get(user_name=a)
        project.members.add(temp_user)
        project.save()

        task = Task()
        task.task_name = 'Moren'
        task.project = project
        task.worker = temp_user
        task.role = 'default role'
        task.save()

        return HttpResponseRedirect(request.session['current_path'])
    except:
         return HttpResponse('error')

@csrf_exempt
def add_task(request, project_id):
    name = request.POST['name']
    task_name = request.POST['task_name']
    task_start = request.POST['task_start']
    task_end = request.POST['task_end']
    task_money = request.POST['task_money']

    # project = Project.objects.get(id=project_id)
    # temp_user = User.objects.get(id = user_id)

    return HttpResponse(name)


@csrf_exempt
def change_role(request):
    role = request.GET['role']
    user = request.GET['user']
    pid = request.GET['pid']
    temp_user = User.objects.get(user_name=user)
    proj = Project.objects.get(id=pid)
    try:
        task = Task.objects.get(task_name='Moren', worker=temp_user, project=proj)
        task.role = role
        task.save()
        return HttpResponse(task.worker.user_name)
    except:
        return HttpResponse("error")

