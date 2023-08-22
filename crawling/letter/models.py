from django.db import models

# Create your models here.
class Letter(models.Model) :
    title = models.CharField(max_length=100)
    write = models.CharField(max_length=100)
    send = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)
    contents = models.TextField(blank=True)

    def __str__(self):
        return self.title