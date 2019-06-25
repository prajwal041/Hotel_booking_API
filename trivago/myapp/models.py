from django.db import models

# Create your models here.
class Solution(models.Model):
    timestamp = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    amenity_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'solution'

    def __unicode__(self):
        return self.user_id

class Clicks(models.Model):
    timestamp = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    hotel_id = models.CharField(max_length=255, blank=True, null=True)
    hotel_region = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'clicks'

    def __unicode__(self):
        return self.hotel_id