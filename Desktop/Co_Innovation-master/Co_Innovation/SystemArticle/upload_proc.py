#!/usr/local/bin/python2.7
#coding=utf-8

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json
import os
import datetime
import time
import hashlib
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile



@csrf_exempt  #取消csrf验证，否则会有403错误
def simditor_file_upload(request):
        files = request.FILES.get('fileData') #得到文件对象
        # return HttpResponse(files.name)
        today = datetime.datetime.today()

        file_dir = settings.MEDIA_ROOT + '/%d/%d/%d/'%(today.year, today.month, today.day)
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)

        s1 = files.name
        s2 = s1[::-1]
        cnt = 0
        for a in s2:
            if a == '.':
                cnt = cnt + 1
                break
            else:
                cnt = cnt + 1

        s3 = s1[:-cnt] + str(int(time.time()))
        s4 = s1[-cnt:]

        #谁能告诉我为啥其他操作都可以,就是一MD5就出错是为啥.
        # f = hashlib.md5()
        # f.update(s3)
        # s3 = f.hexdigest()


        s1 = s3 + s4
        files.name = s1

        file_path = file_dir+files.name
        open(file_path, 'wb+').write(files.read()) #上传文件
        # default_storage.save(file_path, ContentFile(files.read()))
        #得到JSON格式的返回值
        upload_info = {"success": True, 'file_path': settings.MEDIA_URL + '%d/%d/%d/'%(today.year, today.month, today.day) + files.name}
        upload_info = json.dumps(upload_info)

        return HttpResponse(upload_info, content_type="application/json")






