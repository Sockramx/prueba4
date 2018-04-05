from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Categoria(models.Model):
    categoria = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=300, blank=True, null=True)
 
    def __str__(self):
        return self.categoria
        
        
class Link(models.Model):
    web = models.CharField(max_length=100, blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.web
        
        

        
