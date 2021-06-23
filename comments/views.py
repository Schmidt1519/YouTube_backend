from django.shortcuts import render
from .models import Comment
from .models import Reply
from .serializers import CommentSerializer
from .serializers import ReplySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


# Create your views here.
class CommentList(APIView):

    def get(self, request):
        try:
            comment = Comment.objects.all()
            serializer = CommentSerializer(comment, many=True)
            return Response(serializer.data)
        except Comment.DoesNotExist:
            raise Http404

