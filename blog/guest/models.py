from django.db import models

# Create your models here.
class PersonInfo(models.Model):
    account = models.CharField( max_length=20 ,primary_key=True)
    password = models.CharField( max_length=16 )
    nickname = models.CharField( max_length=20,unique=True )
    telno = models.CharField( max_length=11,unique=True )
    email = models.EmailField()
    create_date = models.DateField()
    recent_time = models.TimeField()




