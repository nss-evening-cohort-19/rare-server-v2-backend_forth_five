from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rarev2api.models import Post_Tag, Post, Tag

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
        post = Post.objects.get(pk=request.data["post"])
        tag = Tag.objects.get(pk=request.data["tag"])
        
        post_tag = Post_Tag.objects.create(
            post=post,
            tag=tag
        )
        serializer = PostTagSerializer(post_tag)
        return Response(serializer.data)
    
    def update(self, request, pk):
        post_tag = Post_Tag.objects.get(pk=pk)
        
        post = Post.objects.get(pk=request.data["post"])
        tag = Tag.objects.get(pk=request.data["tag"])
        
        post_tag.post = post
        post_tag.tag = tag
        post_tag.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        post_tag = Post_Tag.objects.get(pk=pk)
        post_tag.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class PostTagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post_Tag
        fields = ('id', 'post', 'tag')
        depth = 1
