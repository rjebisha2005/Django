from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    
#class students(models.Model):
   # name = models.CharField(max_length=100)
    #age = models.IntegerField()
    # mark = models.IntegerField

# class jebii(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     mark = models.IntegerField()


# class Student_ser(models.Model):
#     name = models.CharField(max_length=50)
#     age = models.IntegerField()
#     course = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name
    
    #signals:

class Student_Signals(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

def __str__(self):
    return self.name



