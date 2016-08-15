# -*- coding:utf-8 -*-
from Co_Innovation.wsgi import *
from SystemArticle.models import Article, Column
from ProjectShow.models import Project, Task

def main():
    article_list = Article.objects.filter(category = 'CA')
    summary_part = '这里是写系统文章的摘要'
    for article in article_list:
        article.summary = summary_part + ',系统文章的标题为:{}'.format(article.title)
        article.save()

if __name__ == '__main__':
    main()
    print 'Done!'
