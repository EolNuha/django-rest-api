from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from ..models import Answer
from ..serializers import AnswerSerializer, AnswerCreateSerializer, EmptySerializer
from ..pagination import Pagination


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = Pagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['answer_text', 'author__username']
    
    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return AnswerCreateSerializer
        elif self.action == 'restore':
            return EmptySerializer
        return AnswerSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=False, methods=['post'], url_path="(?P<id>[^/.]+)/restore")
    def restore(self, request, id=None):
        try:
            instance = Answer.everything.get(id=id)
            instance.restore()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Answer.DoesNotExist:
            return Response({'detail': 'Answer not found.'}, status=404)
    
    @action(detail=False, methods=['get'], url_path='by-author/(?P<username>[^/.]+)')
    def by_author(self, request, username=None):
        try:
            user = User.objects.get(username=username)
            answers = Answer.objects.filter(author=user)
            page = self.paginate_queryset(answers)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(answers, many=True)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'detail': 'User not found.'}, status=404)
