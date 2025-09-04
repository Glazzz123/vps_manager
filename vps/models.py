from django.db import models

class VPS(models.Model):
    uid = models.CharField(max_length=100, unique=True)
    cpu = models.IntegerField()
    ram = models.IntegerField()
    hdd = models.IntegerField()
    status = models.CharField(
        max_length=20,
        choices=[('started', 'Started'), ('blocked', 'Blocked'), ('stopped', 'Stopped')],
        default='stopped'
    )

    def __str__(self):
        return self.uid

