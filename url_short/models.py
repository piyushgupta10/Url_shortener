import random
import string
from django.db import models

# Create your models here.

def generate_short_code():
    """Generate a random short code for the URL"""
    return ''.join(string.ascii_letters +string.digits,k=6)

class ShortURL(models.Model):
    original_Url=models.URLField()
    short_code=models.CharField(max_length=10,unique=True,default=generate_short_code)
    created_at=models.DateTimeField(auto_now_add=True)
    expires_at=models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.original_url}-> {self.short_code}"
