# -*- coding:utf-8 -*-
from django import forms
class DateTimeForm(forms.Form):
    course_time = forms.DateTimeField('课程时间');
