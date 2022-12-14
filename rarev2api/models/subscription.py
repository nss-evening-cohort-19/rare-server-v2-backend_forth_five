from django.db import models
from .user import User

class Subscription(models.Model):
    
    follower = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    created_on = models.DateField(auto_now_add=True)
    ended_on = models.DateField()
    
    def __str__(self):
        return self.name
