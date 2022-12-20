from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rarev2api.models import Reaction

class ReactionView(ViewSet):
  
  def retrieve(self, request, pk):
      reaction = Reaction.objects.get(pk=pk)
      serializer = ReeactionSerializer(reaction)
      return Response(serializer.data)
  
  def list(self, request):
      reactions = Reaction.objects.all()
      serializer = ReeactionSerializer(reactions, many = True)
      return Response(serializer.data)
  
  def create(self, request):
    
      reaction = Reaction.objects.create(
      label=request.data["label"],
      image_url=request.data["image_url"]
      )
      serializer = ReeactionSerializer(reaction)
      return Response(serializer.data)
  
  def update(self, request, pk):
    
    reaction = Reaction.objects.get(pk=pk)
    reaction.label = request.data["label"]
    reaction.image_url = request.data["image_url"]
    
    reaction.save()
    
    return Response(None, status=status.HTTP_204_NO_CONTENT)
    
  def destroy(self, request, pk):
      reaction = Reaction.objects.get(pk=pk)
      reaction.delete()
      return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class ReeactionSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Reaction
    fields = ('id', 'label', 'image_url')
    depth = 1
