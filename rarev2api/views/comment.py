from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rarev2api.models import Comment, User

class CommentView(ViewSet):
  
    def retrieve(self, request, pk):
        """Handle GET requests for single comment
        Returns:
            Response -- JSON serialized comment
        """
        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
        

    def list(self, request):
        """"Handle GET requests to handle all comments"""
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
  
class CommentSerializer(serializers.ModelSerializer):
    """JSON serializer for comments
    """
    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'content', 'created_on')
        depth = 1
