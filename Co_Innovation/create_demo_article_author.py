#-*- coding:utf-8 -*-
from Co_Innovation.wsgi import *
from User.models import User
from SystemArticle.models import Column, Article
from ProjectShow.models import Project, Task

def main():
    article_list = Article.objects.all()
    author_list = ['素薇大人', '娅姐', 'Yellow-芬', '喜欢喝鸡尾酒的淦哥哥', '深深爱着老淦的鸡哥', '喜欢给人起别名的Boyce']
    pub_user = User.objects.get(user_name = 'Preke')
    index = 0;
    for article in article_list:
        article.pub_user, article.author = pub_user, author_list[index]
        article.save()
        index = (index + 1) % 6

if __name__ == '__main__':
    main()
    print 'Done!'
