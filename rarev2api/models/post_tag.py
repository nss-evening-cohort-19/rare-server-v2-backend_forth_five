from django.db import models
from .post import Post
from .tag import Tag
class Post_Tag(models.Model):
  
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.name
