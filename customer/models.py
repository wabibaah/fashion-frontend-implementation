import email
from django.db import models

# Create your models here.

class Contact(models.Model):
  name = models.CharField(max_length=50)
  email = models.EmailField()
  phoneNumber = models.CharField(max_length=15)
  description = models.TextField()
  created_at  = models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return f"Message from: {self.email} with number {self.phoneNumber}"
  
# add created at for me to see the time all this happens
