from django.db import models

class Url(models.Model):
    actual = models.CharField(max_length=500)
    shortcode = models.CharField(max_length=100, unique=True)
    last_seen_date = models.DateField(null=True, blank=True)
    redirect_count = models.IntegerField(null=True, blank=True, default=0)
    start_date = models.DateField(null=True, blank=True)