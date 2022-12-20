from django.db import models
from .post import Post
from .tag import Tag
class Post_Tag(models.Model):
  
  post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
  tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)
