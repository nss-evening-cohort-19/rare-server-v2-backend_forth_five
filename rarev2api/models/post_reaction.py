from django.db import models
from .post import Post
from .reaction import Reaction
from .user import User
class Post_Reaction(models.Model):
  
  post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
  reaction_id = models.ForeignKey(Reaction, on_delete=models.CASCADE)
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
