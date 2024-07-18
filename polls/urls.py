from django.urls import path

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet, AnswerViewSet, CustomItemView

router = DefaultRouter()
router.register(r"questions", QuestionViewSet)
router.register(r"answers", AnswerViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("custom-items/", CustomItemView.as_view(), name="custom-items"),
]
