from django.db import models


class Conference(models.Model):
    title = models.CharField(max_length=100)
    edition = models.CharField(max_length=50)

    date_start = models.DateField()
    date_end = models.DateField()

    class Meta:
        ordering = ['date_start']

    def __str__(self):
        return '{0} {1}'.format(self.title, self.edition)
