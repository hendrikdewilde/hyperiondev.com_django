from django.db import models


# Create your models here.
class EmailList(models.Model):
    email = models.EmailField()
    add_date = models.DateTimeField('date added', auto_now=True)

    def __str__(self):
        return "{0}".format(self.email)


class NewsList(models.Model):
    heading = models.CharField(max_length=100)
    article = models.TextField()
    add_date = models.DateTimeField('date added', auto_now=True)

    def __str__(self):
        return self.heading
