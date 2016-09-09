from django.db import models
from django.utils.safestring import mark_safe
from django.utils import timezone
import datetime


class RandomPage(models.Model):
    html_string = models.TextField(default='')
    date_generated = models.DateTimeField(auto_now_add=True, blank=True)
    nsfw = models.BooleanField(default=False)

    def was_generated_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date_generated <= now
