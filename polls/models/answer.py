from django.db import models
from .softdelete import SoftDelete
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from ..models import Question

class Answer(SoftDelete):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_answers", default=1)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers', default=1)
    answer_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.answer_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
