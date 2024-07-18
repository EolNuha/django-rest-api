from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import Answer
from ..serializers import AnswerSerializer
from ..pagination import Pagination


class AnswerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    pagination_class = Pagination
