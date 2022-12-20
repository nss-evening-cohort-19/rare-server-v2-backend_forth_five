from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rarev2api.models import Post_Reaction, User, Reaction, Post

class PostReactionView(ViewSet):
  
  def retrieve(self, request, pk):
    post_reaction = Post_Reaction.objects.get(pk=pk)
    serializer = PostReactionSerializer(post_reaction)
    return Response(serializer.data)
  
  def list(self, request):
      post_reactions = Post_Reaction.objects.all()
      serializer = PostReactionSerializer(post_reactions, many=True)
      return Response(serializer.data)
    
  def create(self, request):
    user = User.objects.get(pk=request.data["user"])
    reaction = Reaction.objects.get(pk=request.data["reaction"])
    post = Post.objects.get(pk=request.data["post"])
    
    post_reaction = Post_Reaction.objects.create(
      user=user,
      reaction=reaction,
      post=post
    )
    serializer = PostReactionSerializer(post_reaction)
    return Response(serializer.data)
  
  def update(self, request, pk):
    post_reaction = Post_Reaction.objects.get(pk=pk)
    
    reaction = Reaction.objects.get(pk=request.data["reaction"])
    post = Post.objects.get(pk=request.data["post"])

    post_reaction.reaction = reaction
    post_reaction.post = post
    post_reaction.save()
    
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
  def destroy(self, request, pk):
    post_reaction = Post_Reaction.objects.get(pk=pk)
    post_reaction.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class PostReactionSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Post_Reaction
    fields = ('id', 'user', 'reaction', 'post')
    depth = 1
