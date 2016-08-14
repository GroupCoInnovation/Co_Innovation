#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
# Create your views here.

def index(request):
    # return render(request, 'Course/index.html')
    # return HttpResponse('Course home')
    request.session['current_path'] = request.path
    return render(request, 'Course/index.html')
