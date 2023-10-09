from django.contrib import admin

from .models import User, Performance, Page, PageInfo, PageNotification, PerformanceList, Calender
# Register your models here.

admin.site.register(User)
admin.site.register(Performance)
admin.site.register(Page)
admin.site.register(PageInfo)
admin.site.register(PageNotification)
admin.site.register(PerformanceList)
admin.site.register(Calender)