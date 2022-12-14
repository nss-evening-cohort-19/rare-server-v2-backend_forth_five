from django.db import models

class Subscription(models.Model):
    
    follower_id = models.ForeignKey(User, on_delete=models.CASCADE)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    created_on = models.DateField(auto_now_add=True)
    ended_on = models.DateField()