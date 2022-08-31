from distutils.command.upload import upload
from django.db import models

# Create your models here.
class AboutSection(models.Model):
    experience_year = models.IntegerField(null=True, blank=True)
    cleint_nums = models.IntegerField(null=True, blank= True)
    num_projects = models.IntegerField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return "About ME"

class Experience_Field(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    level = (
        ('Entry', 'Entry'),
        ('Intermediate', 'Intermediate'),
        ('Experienced', 'Experienced')
    )
    #Fields 
    skill_name = models.CharField(max_length=30, null=True, blank=True)
    levels = models.CharField(max_length=50, choices=level)
    experience_category = models.ForeignKey(Experience_Field, related_name='skills', on_delete=models.CASCADE)

    def __str__(self):
        return self.skill_name
 
class Service_Category(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    service_name = models.CharField(max_length=30, null=True, blank=True)
    service_category = models.ForeignKey(Service_Category, related_name='services', on_delete=models.CASCADE)

    def __str__(self):
        return self.skill_name


class Project(models.Model):
     img = models.ImageField(upload_to='Project_Images')
     title = models.CharField(max_length=50, blank=True, null=True)
     link = models.URLField(null=True, blank=True)
     used_technologies = models.ManyToManyField(Skill, null=True)
     text = models.CharField(max_length=100, null=True, blank=True)

     def __str__(self):
        return self.title
 
class WorkExperience(models.Model):
    company_name = models.CharField(max_length=50, null=True)
    job_title = models.CharField(max_length=30, null=True)
    start_date = models.DateField()
    present = models.BooleanField(default=False,blank=True, null=True)
    end_date = models.DateField()
    text = models.TextField(null=True)
    used_technologies = models.ManyToManyField(Skill, null=True)

    def __str__(self):
        return self.job_title
