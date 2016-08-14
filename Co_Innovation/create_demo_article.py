# -*- coding:utf-8 -*-
from Co_Innovation.wsgi import *
from SystemArticle.models import Article, Column
from datetime import datetime
def main():
    System_column_list = [('行业发展', '解读IT最新时讯,分享业界动态'),
                   ('学术论文', '分享最前沿的学术成果,了解学术大牛的思想'),
                   ('校园IT','引领校园IT风采,绽放学子才华'),
    ]
    for column_name, column_text in System_column_list:
        column = Column.objects.create(category = 'SC' , column_name = column_name, column_text = column_text)
        for i in range(1, 50):
            article = Article()
            article.category = 'SA'
            article.column, article.title = column, 'article_{}'.format(str(i))
            article.content = '我是一只小蜜蜂, 飞到花丛中'
            article.top_time = datetime.now()
            article.save()
        column.save()
        Course_column_list = [('前端技术', '艺术与IT的接吻,让html大方光彩'),
                    ('后台开发','强大的后台以及维护技术,是网站开发的强大引擎'),
                    ('数据库挖掘','数据库与后端的交接,适应用户和前端的数据库模型,是开发网站的核心'),
     ]
    for column_name, column_text in Course_column_list:
        column = Column.objects.create(category = 'CC' , column_name = column_name, column_text = column_text)
        for i in range(1, 50):
            article = Article()
            article.category = 'CA'
            article.column, article.title = column, 'article_{}'.format(str(i))
            article.content = '我是一只小蜜蜂, 飞到花丛中'
            article.top_time = datetime.now()
            article.save()
        column.save()

if __name__ == '__main__':
    main()
    print 'Done!'
