from django.contrib import admin

# from .models import User, Performance, Page, PageInfo, PageNotification, PerformanceList, Calender
# Register your models here.

# admin.site.register(User)
# admin.site.register(Performance)
# admin.site.register(Page)
# admin.site.register(PageInfo)
# admin.site.register(PageNotification)
# admin.site.register(PerformanceList)
# admin.site.register(Calender)
# admin.site.register(UserInfo)


from .models import Page, Page_intro, Page_notice, Page_member, Concert, Concert_location, Calender, Hashtag


# admin.site.register(User)
admin.site.register(Page)
admin.site.register(Page_intro)
admin.site.register(Page_notice)
admin.site.register(Page_member)
admin.site.register(Concert)
admin.site.register(Concert_location)
admin.site.register(Calender)
admin.site.register(Hashtag)
