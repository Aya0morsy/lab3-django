from django.db import models

# Create your models here.
class myuser(models.Model):
    id=models.AutoField(primary_key=True)
    
    password=models.CharField(max_length=16)


    
class myuser1(models.Model):
  id=models.AutoField(primary_key=True)
  name=models.CharField(max_length=10)  
  password=models.CharField(max_length=16)

  def str(self):
      return self.name
        

  empAuth_objects=models.Manager()  

  class add_trainee(models.Model):
      id=models.AutoField(primary_key=True)
      trainee_name=models.CharField(max_length=10)  
      faculty=models.CharField(max_length=16)

class add_trainee1(models.Model):
      id=models.AutoField(primary_key=True)
      trainee_name=models.CharField(max_length=10)  
      faculty=models.CharField(max_length=16)      
      

class track(models.Model):
     id=models.AutoField(primary_key=True)
     track_name=models.CharField(max_length=10) 


class add_trainee2(models.Model):
      id=models.AutoField(primary_key=True)
      trainee_name=models.CharField(max_length=10)  
      faculty=models.CharField(max_length=16)      
      track=models.ForeignKey(track,on_delete=models.CASCADE) 
