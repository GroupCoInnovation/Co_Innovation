#-*- coding:utf-8 -*-
# a context_process

def page_head(request):
    # html_code = '<hr />
    #             {% if is_log_in == False %}
    #             <a href = "{% url 'login' %}" >登录</a>
    #             {% else %}
    #             <a href = "{% url 'log_out' %}">登出</a> {{request.session.user_name}}
    #             {% endif %}
    #             <br/>
    #             <a href =""> <h2> 首页 </h2> </a>
    #             <a href = "Course/index"> 课程课件 </a> &nbsp;&nbsp;
    #             <a href = "ProjectShow/index"> 项目展示 </a> &nbsp;&nbsp;
    #             <a href = "SystemArticle/index"> 系统文章 </a> &nbsp;&nbsp;
    #             <hr>'
    # info = {'page_head':html_code}
    return {'request': request}
