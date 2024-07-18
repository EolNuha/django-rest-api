from django.db import models
from .softdelete import SoftDelete
import datetime
from django.utils import timezone


class Answer(SoftDelete):
    answer_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.answer_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
