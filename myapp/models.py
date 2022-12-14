from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from myapp.formatChecker import ContentTypeRestrictedFileField
from django.core.exceptions import ValidationError

# Create your models here.
class student(models.Model):
    cName = models.CharField(max_length=20, null=False)
    cSex = models.CharField(max_length=2, default='M', null=False)
    cBirthday = models.DateTimeField(null=False)
    cEmail = models.EmailField(max_length=100, blank=True, default='')
    cPhone = models.CharField(max_length=50, blank=True, default='')
    cAddr = models.CharField(max_length=255, blank=True, default='')

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/{1}'.format(instance.cNumber, filename)


class requisition(models.Model):
    cName = models.CharField(max_length=20, default="")
    cNumber = models.CharField(max_length=20, default="")
    cCusetername = models.CharField(max_length=20, null=False)
    cProjectname = models.CharField(max_length=20, null=False)
    cProjectcode = models.CharField(max_length=20, null=False)
    cLocation = models.CharField(max_length=100, default='')
    cContent = models.CharField(max_length=100, default='')
    cLastproject = models.CharField(max_length=100, default='',blank=True)
    cType = models.CharField(max_length=100, default='')
    cCotpye = models.CharField(max_length=100, default='')
    cProjecttype = models.CharField(max_length=100, default='',blank=True)
    cStage = models.CharField(max_length=100, default='')
    cNoted = models.CharField(max_length=100,default='',blank=True)
    cSchedule = models.CharField(max_length=100,default='',blank=True)
    cSpecial = models.CharField(max_length=100,default='',blank=True)
    cdatestart = models.DateField(null=True, blank=True)
    cdateend = models.DateField(null=True, blank=True)
    cFunction = models.CharField(max_length=20, default='')
    title = models.CharField(max_length = 200, default='',blank=True)
    uploadedFile = models.FileField(upload_to=user_directory_path,default='',blank=True)
    dateTimeOfUpload = models.DateTimeField(auto_now = True)
    cStatus = models.CharField(max_length=20, default="In Progress")
    #cVotename = models.ForeignKey(Vote, on_delete=models.CASCADE, default='')
    def __str__(self):
        return self.cNumber
class Vote(models.Model):  #???????????????
    cName =  models.CharField(max_length=10)  #?????????
    #cVotenumber =  models.CharField(max_length=30, null=False)  #?????????
    cVotenumber = models.ForeignKey(requisition, on_delete=models.CASCADE,default='')
    cVoteselect = models.BooleanField(default=False)
    cVotetime =  models.DateTimeField(auto_now = True) #????????????
    def __str__(self):
        return self.cName


class clereply_db(models.Model):
    product = models.CharField(max_length=50, default="")
    checklist = models.CharField(max_length=50, default="")
    producttype = models.CharField(max_length=50, default="")
    productscoreline = models.CharField(max_length=50, default="")

class NewsUnit(models.Model):  #???????????????
	catego =  models.CharField(max_length=10, null=False)  #????????????
	nickname = models.CharField(max_length=20, null=False)  #??????
	title = models.CharField(max_length=50, null=False)  #??????
	message = models.TextField(null=False)  #??????
	pubtime = models.DateTimeField(auto_now=True)  #????????????
	enabled = models.BooleanField(default=False)  #????????????
	press = models.IntegerField(default=0)  #????????????
	def __str__(self):
		return self.title

class Type(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
	    return self.name

class Type2(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
	    return self.name

class AddressInfo(models.Model):
    address = models.CharField(max_length = 30, null = True, blank = True, verbose_name = "Function")
    publications = models.ManyToManyField(Type,default='',blank=True)
    publications2 = models.ManyToManyField(Type2,default='',blank=True)
    def __str__(self):
        return self.address



class Worktype(models.Model):
    worktypenumber = models.IntegerField()
    worktypename = models.CharField(max_length = 10)
    def __str__(self):
        return self.worktypename


class Category(models.Model):
    worktypename = models.ForeignKey('Worktype', on_delete=models.CASCADE,default='') #????????????????????????
    catid = models.IntegerField() #????????????????????????
    categoryname = models.CharField(max_length=50)
    class Meta:
        db_table = 'my_category'
        unique_together = ("catid", "worktypename") #????????????
    def __int__(self):
        return self.categoryname

class Category2(models.Model):
    worktypename = models.ForeignKey('Worktype', on_delete=models.CASCADE,default='') #????????????????????????
    catid = models.IntegerField() #????????????????????????
    categoryname = models.CharField(max_length=50)
    class Meta:
        db_table = 'my_category2'
        unique_together = ("catid", "worktypename") #????????????

class Category3(models.Model):
    worktypename = models.ForeignKey('Worktype', on_delete=models.CASCADE,default='') #????????????????????????
    catid = models.IntegerField() #????????????????????????
    categoryname = models.CharField(max_length=50)
    class Meta:
        db_table = 'my_category3'
        unique_together = ("catid", "worktypename") #????????????