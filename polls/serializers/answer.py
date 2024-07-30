from rest_framework import serializers
from ..models import Answer, Question
from .user import UserSerializer
from .question import QuestionSerializer


class AnswerSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    question = QuestionSerializer(read_only=True)
    class Meta:
        model = Answer
        fields = ['id', 'answer_text', 'pub_date', 'author', 'question']
        
        
class AnswerCreateSerializer(serializers.ModelSerializer):
    question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())

    class Meta:
        model = Answer
        fields = ['id', 'answer_text', 'pub_date', 'question']

class EmptySerializer(serializers.Serializer):
    pass