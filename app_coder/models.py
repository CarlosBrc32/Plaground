from django.db import models


class Course(models.Model):

    name = models.CharField(max_length=40)
    code = models.IntegerField()


class Student(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()


class Profesor(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    profession = models.CharField(max_length=30)


class Homeworks(models.Model):
    name = models.CharField(max_length=30)
    due_date = models.DateField()  
    is_delvered = models.BooleanField()