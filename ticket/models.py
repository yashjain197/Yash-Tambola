from django.db import models

# Create your models here.
class Ticket(models.Model):
    ticket = models.JSONField(null=False, blank=False)
    room_id = models.CharField(max_length=255, null=True, blank=True)
    set_id = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title    