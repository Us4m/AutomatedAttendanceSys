from django.db import models

# Create your models here.

from django.db import models
# Create your models here.
import datetime
import os

class Todo(models.Model):
    text = models.CharField(max_length=40)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename,)
    return os.path.join('uploads/', filename)

class Student(models.Model):
    name = models.CharField(max_length=191,null=True)
    Reg = models.TextField(max_length=50,null=True)
    father_name= models.CharField(max_length=191)
    dob = models.TextField(max_length=191)
    gender = models.TextField(max_length=50)
    ph = models.TextField(max_length=50)
    email = models.TextField(max_length=50)
    cnic = models.TextField(max_length=50)
    nationality = models.TextField(max_length=50)
    status = models.TextField(max_length=50)
    bgroup = models.TextField(max_length=50)
    address = models.TextField(max_length=50)
    image = models.ImageField(upload_to=filepath, null=True, blank=True)

def __str__(self):
        return self.name

        
class Course(models.Model):
    coursename = models.CharField(max_length=191,null=True)
    coursecode = models.TextField(max_length=50,null=True)

class AttendanceImage(models.Model):

    photo = models.ImageField(upload_to="ImagesAttendance")
    date = models.DateTimeField(auto_now_add=True,null=True)

class Contactus(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    utype = models.CharField(max_length=120)
    message = models.CharField(max_length=520)
    
    date = models.DateField()

    def __str__(self) :
        return self.name