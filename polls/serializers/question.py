from rest_framework import serializers
from ..models import Question


class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date', 'author']
        
    def get_author(self, obj):
        return obj.author.username
