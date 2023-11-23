from django.contrib import admin

from .models import Page, Page_intro, Page_notice, Concert, Concert_location, Calender

# admin.site.register(User)
admin.site.register(Page)
admin.site.register(Page_intro)
admin.site.register(Page_notice)
admin.site.register(Concert)
admin.site.register(Concert_location)
admin.site.register(Calender)
