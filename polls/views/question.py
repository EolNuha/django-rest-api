from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from ..models import Question
from ..serializers import QuestionSerializer, EmptySerializer
from ..pagination import Pagination


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    pagination_class = Pagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['question_text', 'author__username']
    
    def get_serializer_class(self):
        if self.action == 'restore':
            return EmptySerializer
        return QuestionSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=False, methods=['post'], url_path="(?P<id>[^/.]+)/restore")
    def restore(self, request, id=None):
        try:
            instance = Question.everything.get(id=id)
            instance.restore()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Question.DoesNotExist:
            return Response({'detail': 'Question not found.'}, status=404)
    
    @action(detail=False, methods=['get'], url_path='by-author/(?P<username>[^/.]+)')
    def by_author(self, request, username=None):
        try:
            user = User.objects.get(username=username)
            questions = Question.objects.filter(author=user)
            page = self.paginate_queryset(questions)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(questions, many=True)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'detail': 'User not found.'}, status=404)
