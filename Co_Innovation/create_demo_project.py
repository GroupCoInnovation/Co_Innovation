#-*- coding:utf-8 -*-
from Co_Innovation.wsgi import *
from User.models import User
from ProjectShow.models import Project, Task
from datetime import datetime

def main():
    project_name_list = ['鸡哥对话', '老淦喝鸡尾酒', '小鸟起飞', '猪八戒游泳', '里约奥运吃翔']
    user_list = User.objects.all()
    for project_name in project_name_list:
        project = Project.objects.create(
            project_name = project_name,
            principal = user_list[1],
        )
        project.members = user_list[1:]
        for n in range(1, 3):
            task_name = 'task_{}_of_{}'.format(str(n),project_name)
            worker = user_list[n]
            task = Task.objects.create(task_name = task_name, project = project, worker = worker)
        project.save()




if __name__ == '__main__':
    main()
    print 'Done!'
