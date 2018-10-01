from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from news.forms import emailForm
from news.models import NewsList


def index(request):
    message = None
    news_list = NewsList.objects.all().order_by("-add_date")[:25]
    if request.method == 'POST':
        form = emailForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Email Address added!!"
            return HttpResponseRedirect(reverse('news_index'))
    else:
        form = emailForm()
    return render(request, 'news/index.html', {'form':form, 'message':message, 'news_list':news_list})
