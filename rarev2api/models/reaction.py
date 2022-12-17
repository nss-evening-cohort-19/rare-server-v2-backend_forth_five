from django.db import models

class Reaction(models.Model):
  
  label = models.CharField(max_length=50)
  image_url = models.URLField(max_length=200)
  
  def __str__ (self):
    return self.name
