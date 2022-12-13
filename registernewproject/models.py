from django.db import models
from building.models import BUILDING
from datetime import datetime, timedelta , date


# Create your models here.
class REGISTERNEWPROJECT(models.Model):
    project_name = models.TextField()
    project_owner = models.TextField()
    project_objective = models.TextField()
    # building = models.ForeignKey(BUILDING,on_delete=models.CASCADE)
    building = models.CharField(max_length=255)
    specific_areas = models.CharField(max_length=255 , null=True)
    related_system = models.TextField()
    owner_area = models.CharField(max_length=255)
    start_project = models.DateTimeField()
    end_project = models.DateTimeField()
    status = models.CharField(max_length=255 , null=True , default="Awaitting Admin Approve")
    approver_1 = models.CharField(max_length=255 ,  null=True)
    approver_2 = models.CharField(max_length=255 ,  null=True)
    approver_3 = models.CharField(max_length=255 ,  null=True)
    
    def __str__(self):
        return self.project_name
    
    
class LOGGING(models.Model):
    Who_Action = models.TextField()
    Action = models.TextField()
    Project = models.TextField()
    Action_Time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.Action_Time 
    
    
    
class SOLARROOFTOP(models.Model):  #  Smart Check Sheet for Substation #1
    tags = models.CharField(max_length=255, null=True)
    inputFile_date = models.DateTimeField(auto_now_add=True)
    endFile_date = models.DateField(default=datetime.now()+timedelta(days=358))
    status = models.CharField(max_length=20 , null=True , default="-")
    file = models.FileField(upload_to = "CheckSheet_Sub1",default="-")
    File_Version2 = models.FileField(upload_to = "CheckSheet_Sub1/File_version2",null=True,default="-")
    File_Version3 = models.FileField(upload_to = "CheckSheet_Sub1/File_version3",null=True,default="-")
    File_Version4 = models.FileField(upload_to = "CheckSheet_Sub1/File_version4",null=True,default="-")
    File_Version5 = models.FileField(upload_to = "CheckSheet_Sub1/File_version5",null=True,default="-")    
    
    def __str__(self):
        return self.file

class PROJECTEE(models.Model):
    tags = models.CharField(max_length=255, null=True)
    inputFile_date = models.DateTimeField(auto_now_add=True)
    endFile_date = models.DateField(max_length=100,default=datetime.now()+timedelta(days=358))
    status = models.CharField(max_length=20 , null=True , default="-")
    file = models.FileField(upload_to = "PROJEAs-build drawing P5 packageCT_EEP5",default="-")
    File_Version2 = models.FileField(upload_to = "As-build drawing P5 package/File_version2",null=True,default="-")
    File_Version3 = models.FileField(upload_to = "As-build drawing P5 package/File_version3",null=True,default="-")
    File_Version4 = models.FileField(upload_to = "As-build drawing P5 package/File_version4",null=True,default="-")
    File_Version5 = models.FileField(upload_to = "As-build drawing P5 package/File_version5",null=True,default="-")
       
    def __str__(self):
        return self.file
    
class MLFAULTDETECTION(models.Model):
    tags = models.CharField(max_length=255, null=True)
    inputFile_date = models.DateTimeField(auto_now_add=True)
    endFile_date = models.DateField(max_length=100,default=datetime.now()+timedelta(days=358))
    status = models.CharField(max_length=20 , null=True , default="-")
    file = models.FileField(upload_to = "DIUDI Improvement",default="-")
    File_Version2 = models.FileField(upload_to = "DIUDI Improvement/File_version2",null=True,default="-")
    File_Version3 = models.FileField(upload_to = "DIUDI Improvement/File_version3",null=True,default="-")
    File_Version4 = models.FileField(upload_to = "DIUDI Improvement/File_version4",null=True,default="-")
    File_Version5 = models.FileField(upload_to = "DIUDI Improvement/File_version5",null=True,default="-")
       
    def __str__(self):
        return self.file

class SMARTCHECKSHEETSUBONE(models.Model):
    tags = models.CharField(max_length=255, null=True)
    inputFile_date = models.DateTimeField(auto_now_add=True)
    endFile_date = models.DateField(max_length=100,default=datetime.now()+timedelta(days=358))
    status = models.CharField(max_length=20 , null=True , default="-")
    file = models.FileField(upload_to = "Smart Check Sheet for Substation1",default="-")
    File_Version2 = models.FileField(upload_to = "Smart Check Sheet for Substation1/File_version2",null=True,default="-")
    File_Version3 = models.FileField(upload_to = "Smart Check Sheet for Substation1/File_version3",null=True,default="-")
    File_Version4 = models.FileField(upload_to = "Smart Check Sheet for Substation1/File_version4",null=True,default="-")
    File_Version5 = models.FileField(upload_to = "Smart Check Sheet for Substation1/File_version5",null=True,default="-")
       
    def __str__(self):
        return self.file
