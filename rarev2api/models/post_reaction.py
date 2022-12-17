from django.db import models
from .post import Post
from .reaction import Reaction
class Post_Reaction(models.Model):
  
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  reaction = models.ForeignKey(Reaction, on_delete=models.CASCADE)
