from django.db import models
from .user import User

class Prediction(models.Model):
    id              = models.AutoField(primary_key=True)
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    created         = models.DateTimeField(auto_now_add=True, blank=True)
    age             = models.IntegerField()
    pregnancies     = models.IntegerField()
    glucose         = models.FloatField()
    bloodpreassure  = models.FloatField()
    insulin         = models.FloatField()
    bmi             = models.FloatField()
    tskinthickness  = models.FloatField()
    dpedigreefunc   = models.FloatField(default=0.47, blank=True)
    rta             = models.BooleanField(default=False, blank=True)