from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rarev2api.models import Subscription, User

class SubscriptionView(ViewSet):
  
  def retrieve(self, request, pk):
    subscription = Subscription.objects.get(pk=pk)
    serializer = SubscriptionSerializer(subscription)
    return Response(serializer.data)
  
  def list(self, request):
      subscriptions = Subscription.objects.all()
      serializer = SubscriptionSerializer(subscriptions, many=True)
      return Response(serializer.data)
    
  def create(self, request):
    follower = User.objects.get(pk=request.data["follower"])
    author = User.objects.get(pk=request.data["author"])
    
    subscription = Subscription.objects.create(
      follower=follower,
      author=author,
      created_on=request.data["created_on"],
      ended_on=request.data["ended_on"]
    )
    serializer = SubscriptionSerializer(subscription)
    return Response(serializer.data)
  
  def update(self, request, pk):
    subscription = Subscription.objects.get(pk=pk)
    
    follower = User.objects.get(pk=request.data["follower"])
    author = User.objects.get(pk=request.data["author"])

    subscription.follower=follower
    subscription.author=author
    subscription.created_on=request.data["created_on"]
    subscription.ended_on=request.data["ended_on"]
    subscription.save()
    
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
  def destroy(self, request, pk):
    subscription = Subscription.objects.get(pk=pk)
    subscription.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class SubscriptionSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Subscription
    fields = ('id', 'follower', 'author', 'created_on', 'ended_on')
    depth = 1
