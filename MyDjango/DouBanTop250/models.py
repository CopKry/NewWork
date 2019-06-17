from django.db import models
class douban(models.Model):
    id=models.BigIntegerField
    d_name=models.CharField(max_length=255,blank=True,null=True)
    d_other=models.CharField(max_length=255,blank=True,null=True)
    d_direct=models.CharField(max_length=255,blank=True,null=True)
    d_year=models.CharField(max_length=255,blank=True,null=True)
    d_from=models.CharField(max_length=255,blank=True,null=True)
    d_type=models.CharField(max_length=255,blank=True,null=True)
    d_content=models.CharField(max_length=255,blank=True,null=True)


    def __str__(self):
        return self.id