from django.db import models

from accounts.models import User
from calendarapp.models import Event, EventAbstract

class Routine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="routine")
    name = models.CharField(max_length=75)
    privacity = models.BooleanField(default=True)

class RoutineEvents(Event):
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE,related_name="routine_events")
    
    