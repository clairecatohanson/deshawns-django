from django.db import models


class Appointment(models.Model):
    completed = models.BooleanField(default=False)
    date = models.DateField()
    walker = models.ForeignKey(
        "Walker", on_delete=models.CASCADE, related_name="appointments"
    )
