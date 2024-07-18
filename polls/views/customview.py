from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class CustomItemView(APIView):
    # Require authentication for this view
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="GET /custom-items/",
        responses={
            200: openapi.Response(
                "description", openapi.Schema(type=openapi.TYPE_OBJECT)
            )
        },
    )
    def get(self, request, format=None):
        # Example logic for a GET request
        data = {"message": "This is a custom GET endpoint", "items": []}
        return Response(data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="POST /custom-items/",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "field1": openapi.Schema(
                    type=openapi.TYPE_STRING, description="field1 description"
                ),
                "field2": openapi.Schema(
                    type=openapi.TYPE_STRING, description="field2 description"
                ),
            },
        ),
        responses={
            201: openapi.Response(
                "description", openapi.Schema(type=openapi.TYPE_OBJECT)
            )
        },
    )
    def post(self, request, format=None):
        # Example logic for a POST request
        data = {
            "message": "This is a custom POST endpoint",
            "received_data": request.data,
        }
        return Response(data, status=status.HTTP_201_CREATED)
