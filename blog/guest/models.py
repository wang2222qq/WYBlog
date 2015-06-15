#coding:utf-8
from django.db import models

# Create your models here.
##class PersonInfo(models.Model):
##    account = models.CharField( max_length=20 ,primary_key=True)
##    password = models.CharField( max_length=16 )
##    nickname = models.CharField( max_length=20,unique=True )
##    telno = models.CharField( max_length=11,unique=True )
##    email = models.EmailField()
##    create_date = models.DateField()
##    recent_time = models.TimeField()

class Comment(models.Model):
#评论_id
    comment_id = models.IntegerField( primary_key=True )
#昵称
    nickname = models.CharField( max_length=20 )
#内容
    contents = models.CharField( max_length=200 )
#创建时间
    create_time = models.DateTimeField()
#关联uuid
    forgein_id = models.IntegerField()

class Article(models.Model):
#文章id
    article_id = models.IntegerField( primary_key=True )
#标题
    title = models.CharField( max_length=60 )
#发表日期
    pub_time = models.DateTimeField()
#标签
    lable = models.CharField( max_length=60 )
#浏览次数
    browes_number = models.IntegerField()


class Photoalbum(models.Model):
    album_id = models.IntegerField( primary_key=True )
    Name = models.CharField( max_length=60 )
    pub_time = models.DateTimeField()


class Photograph(models.Model):
#相片id
    photo_id = models.IntegerField( primary_key=True )
#相片名字
    name = models.CharField( max_length=60 )
#相片地址
    image_address = models.FileField()
#出版日期
    pub_time = models.DateTimeField()
#浏览次数
    browes_number = models.IntegerField()

    
    




