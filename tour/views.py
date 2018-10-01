from django.shortcuts import render

from tour.models import TourList


# Create your views here.
def index(request):
    tour_list = TourList.objects.all().order_by("date")[:25]
    return render(request, 'tour/index.html', {'tour_list':tour_list})
