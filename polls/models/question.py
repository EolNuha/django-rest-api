from django.db import models
from .softdelete import SoftDelete
import datetime
from django.utils import timezone
from django.contrib.auth.models import User


class Question(SoftDelete):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_questions", default=1)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
