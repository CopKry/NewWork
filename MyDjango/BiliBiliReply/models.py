from django.db import models
class bilibili(models.Model):
    id=models.BigIntegerField
    user=models.CharField(max_length=255,blank=True,null=True)
    reply=models.CharField(max_length=500,blank=True,null=True)
    floor=models.CharField(max_length=255,blank=True,null=True)
    time=models.CharField(max_length=255,blank=True,null=True)
    

    def __str__(self):
        return self.id
