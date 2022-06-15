from apps.accounts.models import Account
from django.contrib.auth.models import User
from django.db import models


class Measurement(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="measurements")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "Measurement " + str(self.id) + " by " + self.account.first_name + " " + self.account.last_name

class MeasurementPoint(models.Model):

    measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE, related_name="measurement_points")

    time_stamp = models.DateTimeField()

    ENGINE_LOAD = models.FloatField(blank=True, null=True)
    RPM = models.FloatField(blank=True, null=True)
    MAF = models.FloatField(blank=True, null=True)
    SPEED = models.FloatField(blank=True, null=True)
    THROTTLE_POS = models.FloatField(blank=True, null=True)



