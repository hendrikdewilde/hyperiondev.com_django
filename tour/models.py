from django.db import models


# Create your models here.
class TourList(models.Model):
    date = models.DateField()
    place = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return "<b>{0}: {1}</b><br>{2}".format(self.date, self.place, self.description)
