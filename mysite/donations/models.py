from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="event_images/", blank=True, null=True)

    class Meta:
        ordering = ["date", "time"]

    def __str__(self) -> str:
        return self.title

