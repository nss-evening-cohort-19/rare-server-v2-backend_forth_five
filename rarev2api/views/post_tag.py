from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rarev2api.models import Post_Tag

class PostTagView(ViewSet):
    
    def retrieve(self, request, pk):
        post_tag = Post_Tag.objects.get(pk=pk)
        serializer = PostTagSerializer(post_tag)
        return Response(serializer.data)
    
    def list(self, request):
        post_tags = Post_Tag.objects.all()
        serializer = PostTagSerializer(post_tags, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        post_tag = Post_Tag.objects.create(
            post_id=request.data["post_id"],
            tag_id=request.data["tag_id"]
        )
        serializer = PostTagSerializer(post_tag)
        return Response(serializer.data)
    
    def update(self, request, pk):
        post_tag = Post_Tag.objects.get(pk=pk)
        post_tag.post_id = request.data["post_id"]
        post_tag.tag_id = request.data["tag_id"]
        post_tag.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        post_tag = Post_Tag.objects.get(pk=pk)
        post_tag.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class PostTagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post_Tag
        fields = ('id', 'post_id', 'tag_id')
        depth = 1
