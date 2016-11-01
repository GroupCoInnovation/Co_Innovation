# -*- coding:utf-8 -*-
from Co_Innovation.wsgi import *
from Course.models import Course
from SystemArticle.models import Article, Column
from datetime import datetime
content = 'Python数据挖掘实战，简单、实用的Python数据挖掘视频教程。主要介绍Python在数据处理、挖掘方面的实战方法技巧。Python数据挖掘实战，简单、实用的Python数据挖掘视频教程。主要介绍Python在数据处理、挖掘方面的实战方法技巧。'
def main():
    column = Column.objects.filter(category = 'CC')[0]
    for i in range(1, 48):
        course = Course()
        course.column = column
        course.title = '课程_{}'.format(str(i))
        course.course_intro = content
        course.place = '公交楼D301'
        course.time = datetime.now()
        course.save()


def update():
    course_list = Course.objects.all()
    for course in course_list:
        course.course_intro = content
        course.save()
if __name__ == '__main__':
    main()
    print 'Done!'
