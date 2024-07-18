import datetime
from django.test import TestCase
from django.utils import timezone
from ..models import Answer


class AnswerModelTests(TestCase):
    def test_was_published_recently_with_future_answer(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_answer = Answer(pub_date=time)
        self.assertIs(future_answer.was_published_recently(), False)

    def test_was_published_recently_with_old_answer(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_answer = Answer(pub_date=time)

        self.assertIs(old_answer.was_published_recently(), False)

    def test_was_published_recently_with_recent_answer(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_answer = Answer(pub_date=time)

        self.assertIs(recent_answer.was_published_recently(), True)
