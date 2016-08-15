#-*- coding:utf-8 -*-
from django.shortcuts import render
from User.models import User
from django.http import HttpResponse
import hashlib
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
# Create your views here.
# def home_user(request, user_id, password):
#     try:
#         user = User.objects.get(pk = user_id)
#         f = hashlib.md5()
#         f.update(password)
#         password = f.hexdigest()
#         if user.password != password:
#             raise DoesNotExit
#             info = {'user_name':user.us|er_name}
#         return render(request, 'User/home_user.html', info)
#     except:
#         return HttpResponse('Information Error')

def register(request):
    create_user_root = 16
    if not (request.session.get('root', 0) & create_user_root):
        return HttpResponse("You don't have privilege to create a user")
    if request.method == 'GET':
        return render(request, 'User/register.html')
    else :
        user_name, password = request.POST['user_name'], request.POST['password']
        f = hashlib.md5()
        f.update(password)
        password = f.hexdigest()
        user, not_exist = User.objects.get_or_create(user_name = user_name)
        if not_exist:
            user.password = password
            user.save()
            return HttpResponseRedirect(request.session['current_path'])
        else :
            return HttpResponse('the user has existed!')

def login(request):
    # if request.method == 'GET':
    #     return render(request, 'User/login.html')
    # else :  #POST
    try:
        user_name, password = request.POST['user_name'], request.POST['password']
        f = hashlib.md5()
        f.update(password)
        password = f.hexdigest()
        user= User.objects.get(user_name = user_name, password = password)
        info = {'user_name':user_name, 'password':password}
        #return HttpResponse('success')
        request.session['user_name'] = user.user_name
        request.session['root'] = user.root
        return HttpResponseRedirect(request.session['current_path'])  #  should change to return the current page
    except:
        return HttpResponse('Information Error')

def log_out(request):
    try:
        del request.session['user_name']
        del request.session['root_write']
        del request.session['root_edit']
        del request.session['root_stick']
        del request.session['root_create']
        del request.session['root']
    except:
        pass
    return HttpResponseRedirect(request.session['current_path'])

# 登录验证和编辑用户权限
def edit_root(request):
    edit_root_root = 32
    if request.method == 'GET':
        if not (request.session.get('root', 0) & edit_root_root):
            return HttpResponse("you don't have the privilege to edit a user's root")
        return render(request, 'User/edit_root_log.html')
    else : #POST
        write_root, edit_article_root, stick_root, create_user_root, edit_root_root = 2, 4, 8, 16, 32
        user_name = request.POST.get('user_name', None)
        if user_name == None:
            return HttpResponse("Error")
        try:
            # 待编辑用户
            user_to_edit = User.objects.get(user_name = user_name) # the user whose root is edited
            # 编辑权限的用户
            user = User.objects.get(user_name = request.session['user_name']) # the user who has the privilege to edit
            info = {'user':user_to_edit, 'roots_edit':[], 'roots_not_change':[], 'roots_not_change_all':0}
            root_list = [('写文章', 2), ('编辑文章', 4), ('置顶', 8), ('开用户', 16),('编辑用户权限', 32)]
            for root_name , root in root_list:
                if user_to_edit.root & root:
                    info['roots_not_change'].append((root_name, root))
                if (user.root & root): # 可编辑的权限
                    info['roots_edit'].append((root_name, root))
                else: # 不可编辑的权限
                    info['roots_edit'].append((root_name, 0))
                    if user_to_edit.root & root: #待编辑用户独有的权限, 直接把值加到 roots_not_change_all
                        info['roots_not_change_all'] += root
            return render(request, 'User/edit_root.html', info)
        except:
            return HttpResponse('Error')

def edit_root_process(request):
    try:
        root = int(request.POST.get('root_1', 0)) + int(request.POST.get('root_2', 0)) + int(request.POST.get('root_3', 0))
        root += int(request.POST.get('root_4', 0)) + int(request.POST.get('root_5', 0))
        # 再加上待编辑用户独有的权限的总值S
        root += int(request.POST.get('roots_not_change_all', 0))
        user_name = request.POST.get('user_name', 0)
        user = User.objects.get(user_name = user_name)
        user.root = root
        user.save()
        return HttpResponseRedirect(request.session['current_path'])
    except:
        return HttpResponse('Error')

def find(request):
    try:
        user_name = request.GET['user_name']
        user = User.objects.get(user_name = user_name)
        return HttpResponse("exist")
    except:
        return HttpResponse("not exist")
