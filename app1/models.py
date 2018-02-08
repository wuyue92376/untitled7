from django.db import models

# Create your models here.
class userInfo(models.Model):
    username = models.CharField(max_length=60)
    passwd = models.CharField(max_length=60)
    user_group=models.ForeignKey('userGroup',to_field='uid',default=1)
    email = models.CharField(max_length=60)
class userGroup(models.Model):
    uid =models.AutoField(primary_key=True)
    groups = models.CharField(max_length=60)
class HostInfo(models.Model):
    HostIP =models.GenericIPAddressField(db_index=True)
    Hostname = models.CharField(max_length=30,db_index=True)
    version=models.CharField(max_length=30)
    app = models.ForeignKey(to="appInfo",to_field="id",null=True)
    admin=models.CharField(max_length=30,null=True)
    passwd=models.CharField(max_length=60,null=True)
class appInfo(models.Model):
    proline = models.CharField(max_length=30,db_index=True)