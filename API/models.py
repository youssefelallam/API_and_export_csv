from django.db import models



class Prod(models.Model):
    title = models.CharField(max_length=200,null=True)
    date = models.DateField(auto_now_add=True)
    startTime = models.TimeField(auto_now_add=True)
    endTime = models.TimeField(default=None, blank=True, null=True)
    complit = models.BooleanField(default=False)

    def __str__(self):
        return self.title