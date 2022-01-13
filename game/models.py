from django.db import models

# Create your models here.
class Game(models.Model):
    id              = models.BigIntegerField(primary_key=True)
    seriesId        = models.BigIntegerField()
    result          = models.CharField(max_length = 100)
    event_date      = models.DateField()
    title           = models.CharField(max_length = 512)
    date_created    = models.DateTimeField(auto_now_add=True)
    last_modified   = models.DateTimeField(auto_now=True)

    def __str___(self):
        return self.title