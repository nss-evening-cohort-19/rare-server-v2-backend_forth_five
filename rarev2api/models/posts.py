from django.db import models
from .user import User
from .category import Category

class Event(models.Model):
  
    user_id = models.ForeignKey(UserId, on_delete=models.CASCADE)
    category_id = models.ForeignKey(CategoryId, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    publication_date = models.DateField(auto_now=True)
    image_url = models.URLField(max_length=200)
    content = models.CharField(max_length=1000)
    approved = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    