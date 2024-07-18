from rest_framework import viewsets
from ..models import Question
from ..serializers import QuestionSerializer
from ..pagination import Pagination


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    pagination_class = Pagination
