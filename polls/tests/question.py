import datetime
from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from ..models import Question


class QuestionModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time, author=self.user)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time, author=self.user)

        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time, author=self.user)

        self.assertIs(recent_question.was_published_recently(), True)

    def test_create_question(self):
        """
        Test creating a Question.
        """
        question = Question.objects.create(
            question_text="What's new?", pub_date=timezone.now(), author=self.user
        )
        self.assertEqual(Question.objects.count(), 1)
        self.assertEqual(question.question_text, "What's new?")
        self.assertTrue(question.was_published_recently())

    def test_read_question(self):
        """
        Test reading a Question.
        """
        question = Question.objects.create(
            question_text="What's new?", pub_date=timezone.now(), author=self.user
        )
        retrieved_question = Question.objects.get(pk=question.pk)
        self.assertEqual(retrieved_question.question_text, "What's new?")
        self.assertTrue(retrieved_question.was_published_recently())

    def test_update_question(self):
        """
        Test updating a Question.
        """
        question = Question.objects.create(
            question_text="What's new?", pub_date=timezone.now(), author=self.user
        )
        question.question_text = "What's updated?"
        question.save()
        updated_question = Question.objects.get(pk=question.pk)
        self.assertEqual(updated_question.question_text, "What's updated?")

    def test_soft_delete_question(self):
        """
        Test soft deleting a Question.
        """
        question = Question.objects.create(
            question_text="What's new?", pub_date=timezone.now(), author=self.user
        )
        question.delete()
        self.assertEqual(Question.objects.filter(pk=question.pk).count(), 0)
        self.assertEqual(Question.everything.filter(pk=question.pk).count(), 1)
        self.assertTrue(Question.everything.get(pk=question.pk).is_deleted)

    def test_restore_deleted_question(self):
        """
        Test restoring a soft deleted Question.
        """
        question = Question.objects.create(
            question_text="What's new?", pub_date=timezone.now(), author=self.user
        )

        question.delete()
        self.assertEqual(Question.objects.filter(pk=question.pk).count(), 0)

        question.restore()
        self.assertEqual(Question.objects.filter(pk=question.pk).count(), 1)
        self.assertFalse(Question.objects.get(pk=question.pk).is_deleted)
