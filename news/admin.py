from django.contrib import admin

# Register your models here.
from news.models import EmailList, NewsList


class EmailListAdmin(admin.ModelAdmin):
    list_display = ['email', 'add_date']


admin.site.register(EmailList, EmailListAdmin)


class NewsListAdmin(admin.ModelAdmin):
    list_display = ['heading', 'article', 'add_date']


admin.site.register(NewsList, NewsListAdmin)
