from django.contrib import admin

# Register your models here.
from tour.models import TourList


class TourListAdmin(admin.ModelAdmin):
    list_display = ['date', 'place', 'description']


admin.site.register(TourList, TourListAdmin)

