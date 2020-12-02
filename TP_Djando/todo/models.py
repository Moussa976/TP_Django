from django.db import models

# Create your models here.
class Task(models.Model):  
    content = models.CharField(max_length=255)  
    is_done = models.BooleanField()  
    created_date = models.DateTimeField() 
  
    class Meta:  
        db_table = "task"