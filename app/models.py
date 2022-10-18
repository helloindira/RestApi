from django.db import models

# Create your models here.

class Paradigm(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name 

class Language(models.Model):
    name = models.CharField(max_length=255) 
    paradigm = models.ForeignKey(Paradigm,on_delete = models.CASCADE)

    def __str__(self):
        return self.name 

class Programmer(models.Model):
    name = models.CharField(max_length=255)
    languages = models.ForeignKey(Paradigm,on_delete = models.CASCADE)

def __str__(self):
        return self.name 