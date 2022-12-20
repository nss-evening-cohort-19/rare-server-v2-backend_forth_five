from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rarev2api.models import Post, User, Category

class PostView(ViewSet):

    def retrieve(self, request, pk):
        
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def list(self, request):

        posts = Post.objects.all()
        uid = request.query_params.get('type', None)
        if uid is not None:
          posts = posts.filter(user_id=uid)  
        serializer = PostSerializer(posts, many = True)
        return Response(serializer.data)

    def create(self, request):

        User = User.objects.get(pk=request.data["user_id"])
    
        post = Post.objects.create(
        title=request.data["title"],
        publication_date=request.data["publication_date"],
        content=request.data["content"],
        approved=request.data["approved"],
        user_id =User
        )
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def update(self, request, pk):

        post = Post.objects.get(pk=pk)
        post.title = request.data["title"]
        post.publication_date = request.data["publication_date"]
        post.content = request.data["content"]
        post.approved = request.data["approved"]
        
        #The below is for when we incorp categories 
        category = Category.objects.get(pk=request.data["category"])
        post.category = category
        post.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)  

    def destroy(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)    

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ('id', 'user_id', 'title', 'publication_date', 'content', 'approved') 
        depth = 1
