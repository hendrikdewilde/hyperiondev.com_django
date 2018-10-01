from django.forms import ModelForm

from news.models import EmailList


class emailForm(ModelForm):
    class Meta:
        model = EmailList
        fields = ('email',)



