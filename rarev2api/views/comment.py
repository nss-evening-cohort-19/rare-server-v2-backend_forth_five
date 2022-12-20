from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rarev2api.models import Comment, User, Post

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
    
    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized game instance
        """
        comment = Comment.objects.get(uid=request.data["user_id"])

        comment = Comment.objects.create(
            author_id=request.data["author_id"],
            post_id=request.data["post_id"],
            content=request.data["content"]
        )
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a comment
        Returns:
            Response -- Empty body with 204 status code
        """

        comment = Comment.objects.get(pk=pk)
        comment.author_id = request.data["author_id"]
        comment.post_id = request.data["post_id"]
        comment.content = request.data["content"]
        comment.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
  
class CommentSerializer(serializers.ModelSerializer):
    """JSON serializer for comments
    """
    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'content', 'created_on')
        depth = 1
