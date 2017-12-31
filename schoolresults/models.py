from django.db import models
from django.core.urlresolvers import reverse
from django.db.models import permalink


class student(models.Model):
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=80)
    password = models.CharField(max_length=80)
    
    @permalink
    def save_semester(self):
        return ("save-semester" , None , {"email":self.email})
    @permalink
    def add_semester(self):
        return ("semester-add",None,{"email":self.email})
    @permalink
    def logout(self):
        return ("index",None)
    @permalink
    def profile(self):
        return ("profile",None,{"email":self.email})
    def __str__(self):
        return self.name
    
class semester(models.Model):
    student = models.ForeignKey(student , on_delete = models.CASCADE)
    name = models.CharField(max_length = 80)
    
    
    @permalink
    def show(self):
        return ("show-semester" , None , {"name" : self.name , "user":self.student})
        
    
class marks(models.Model):
    semester = models.ForeignKey(semester , on_delete = models.CASCADE)
    
    English_class = models.FloatField(default=0)
    English_exam = models.FloatField(default=0)
    English_result = models.FloatField(default=0)
    Science_class = models.FloatField(default=0)
    Science_exam = models.FloatField(default=0)
    Science_result = models.FloatField(default=0)
    social_class = models.FloatField(default=0)
    social_exam = models.FloatField(default=0)
    social_result = models.FloatField(default=0)
    maths_class = models.FloatField(default=0)
    maths_exam = models.FloatField(default=0)
    maths_result = models.FloatField(default=0)
    
    
    @permalink
    def get_marks(self):
        return ("" , None , {"slug":self.Slug})
    
    