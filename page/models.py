from django.db import models

class ParkInfo(models.Model):
    slot_status = models.TextField()

    def __str__(self):
        return 'status'

