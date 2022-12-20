from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rarev2api.models import User

class UserView(ViewSet):


    def retrieve(self, request, pk):

        try:
            user = User.objects.get(pk=pk)
            serializer = Userserializer(user)
            return Response(serializer.data)
        except User.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):

        users = User.objects.all()
        serializer = Userserializer(users, many=True)
        return Response(serializer.data)

    def create(self, request):

        user = User.objects.create(
            first_name=request.data["first_name"],
            last_name=request.data["last_name"],
            bio=request.data["bio"],
            profile_image_url=request.data["profile_image_url"],
            email=request.data["email"],
            created_on=request.data["created_on"],
            active=request.data["active"],
            is_staff=request.data["is_staff"],
            uid=request.data["uid"],
        )
        serializer = Userserializer(user)
        return Response(serializer.data)

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('uid', 'first_name', 'last_name', 'bio', 'profile_image_url', 'email', 'created_on', 'active', 'is_staff')
        depth = 1
