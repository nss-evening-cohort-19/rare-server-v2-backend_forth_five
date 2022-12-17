from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rarev2api.models import Post_Reaction

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
    post_reaction = Post_Reaction.objects.create(
      user_id=request.data["user_id"],
      reaction_id=request.data["reaction_id"],
      post_id=request.data["post_id"]
    )
    serializer = PostReactionSerializer(post_reaction)
    return Response(serializer.data)
  
  def update(self, request, pk):
    post_reaction = Post_Reaction.objects.get(pk=pk)
    post_reaction.user_id = request.data["user_id"]
    post_reaction.reaction_id = request.data["reaction_id"]
    post_reaction.post_id = request.data["post_id"]
    post_reaction.save()
    
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
  def destroy(self, request, pk):
    post_reaction = Post_Reaction.objects.get(pk=pk)
    post_reaction.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class PostReactionSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Post_Reaction
    fields = ('id', 'user_id', 'reaction_id', 'post_id')
    depth = 1
