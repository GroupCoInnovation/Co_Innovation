from django.contrib import admin
from ProjectShow.models import Project, Task
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'principal', 'status', 'start_time', 'deadline']
    search_fields = ['project']
    list_filter = ['status', 'start_time', 'principal']

class TaskAdmin(admin.ModelAdmin):
    list_display = ['task_name', 'project', 'worker', 'is_finished']
    list_filter = ['project', 'worker']
    search_fields = ['task_name']

admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
