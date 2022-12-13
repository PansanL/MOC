from datetime import datetime
from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from .models import REGISTERNEWPROJECT,SOLARROOFTOP,PROJECTEE,LOGGING, MLFAULTDETECTION ,SMARTCHECKSHEETSUBONE
from django.contrib.auth.models import auth
from datetime import datetime, timedelta , date
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/loginsystem/")
def home(request):
    return redirect("panel")

@login_required(login_url="/loginsystem/")
def insertData (request):
    user = auth.get_user(request)
    if request.method == "POST" :
        # image = request.FILES["image"]
        # รับค่าจาก Form
        project_name = request.POST["Project Name"] # Project Name คือ name ที่เราตั้งชื่อใน HTML File
        project_objective = request.POST["Objective Project"]
        project_owner = request.POST["Project Owner"]
        building = request.POST["Building"]
        specific_areas = request.POST["Specific Areas"]
        related_system = request.POST["Related System"]
        owner_area = request.POST["Owner Area"]
        start_project = request.POST["Start Project"]
        end_project = request.POST["End Project"]
        # approver_1 = request.POST["approver_1"]
        # approver_2 = request.POST["approver_2"]
        # approver_3 = request.POST["approver_3"]
        # endFile_date = datetime.now() + timedelta(days=5)
        
        fs = FileSystemStorage()
        # Uploads
        # image_url = "design_image/" + image.name
        # filename = fs.save(image_url , image)
        
        # บันทึกข้อมูล
        registernewproject = REGISTERNEWPROJECT(project_name=project_name, 
                                                project_owner=project_owner,
                                                project_objective= project_objective,
                                                related_system=related_system,
                                                owner_area=owner_area,
                                                start_project=start_project,
                                                end_project=end_project,
                                                building=building,
                                                specific_areas=specific_areas,

                                                )                                                                                                                                                                                  
                                                
        registernewproject.save()    
        return redirect("panel")

@login_required(login_url="/loginsystem/")
def allproject(request):
    allproject = REGISTERNEWPROJECT.objects.filter(status = 'Approve')
    return render(request,"Frontend/allproject.html",{"allproject":allproject})

@login_required(login_url="/loginsystem/")
def Dashboard(request):
    # >>>>> For Chart 1 <<<<< #
    ALL_Approved = REGISTERNEWPROJECT.objects.filter(status = 'Approve')
    QTY_building1 = ALL_Approved.filter(building__contains='1').count()
    QTY_building2 = ALL_Approved.filter(building__contains='2').count()
    QTY_building3 = ALL_Approved.filter(building__contains='3').count()
    QTY_building4 = ALL_Approved.filter(building__contains='4').count()
    QTY_building5 = ALL_Approved.filter(building__contains='5').count()
    
    # >>>>> For Chart 2 <<<<< #
    ThisYear = REGISTERNEWPROJECT.objects.filter(end_project__year = '2022')
    Jan = ThisYear.filter(end_project__month='01').count()  
    Feb = ThisYear.filter(end_project__month='02').count()  
    Mar = ThisYear.filter(end_project__month='03').count()  
    Apr = ThisYear.filter(end_project__month='04').count()  
    May = ThisYear.filter(end_project__month='05').count()
    Jun = ThisYear.filter(end_project__month='06').count()  
    Jul = ThisYear.filter(end_project__month='07').count()  
    Aug = ThisYear.filter(end_project__month='08').count()  
    Sep = ThisYear.filter(end_project__month='09').count()  
    Oct = ThisYear.filter(end_project__month='10').count()  
    Nov = ThisYear.filter(end_project__month='11').count()  
    Dec = ThisYear.filter(end_project__month='12').count()  
    
    # >>>>> For Chart 3 <<<<< #
    ExpiredFile_Solar = SOLARROOFTOP.objects.filter(endFile_date__lte = datetime.now()).count() # lte = less than or equal
    
    # >>>>> For Chart 4 <<<<< #
    Awaiting_Approval_Solar = SOLARROOFTOP.objects.filter(status = '-').count()
    Awaiting_Approval_ML = MLFAULTDETECTION.objects.filter(status = '-').count()
    
    month = [Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec]    
    # Month_Solar = [jan_solar, feb_solar, mar_solar, apr_solar, may_solar, jun_solar, jul_solar, aug_solar, sep_solar, oct_solar, nov_solar, dec_solar]
    qtyproject_list = [QTY_building1,QTY_building2,QTY_building3,QTY_building4,QTY_building5]
    return render(request,"Frontend/Dashboard.html",{"qtyproject_list":qtyproject_list,"month":month,"ExpiredFile_Solar":ExpiredFile_Solar,"Awaiting_Approval_Solar":Awaiting_Approval_Solar,"Awaiting_Approval_ML":Awaiting_Approval_ML})

    
@login_required(login_url="/loginsystem/")
def Access_Project(request,id):  
    allproject = REGISTERNEWPROJECT.objects.filter(id= id) # For receive project_name
    SolarRoofTop = SOLARROOFTOP.objects.all() # Smart Check Sheet for Substation #1
    TestProject_EE =PROJECTEE.objects.all()
    ML_Fault = MLFAULTDETECTION.objects.all()
    CheckSheet_Sub1 = SMARTCHECKSHEETSUBONE.objects.all()
    # Check Condition Before Query
    if id == 1: # Smart Check Sheet for Substation #1
        return render(request,"Frontend/Access_Project.html",{"allproject":allproject,"SolarRoofTop":SolarRoofTop})
    elif id == 2:
        return render(request,"Frontend/Access_Project.html",{"allproject":allproject,"TestProject_EE":TestProject_EE})
    elif id == 3:
        return render(request,"Frontend/Access_Project.html",{"allproject":allproject,"ML_Fault":ML_Fault})
    elif id == 4:
        return render(request,"Frontend/Access_Project.html",{"allproject":allproject,"CheckSheet_Sub1":CheckSheet_Sub1})
    
    
@login_required(login_url="/loginsystem/")
def logging (request):
    logging =  LOGGING.objects.all()
    return render(request,"Frontend/logging.html",{"logging":logging})

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Smart Check Sheet for Substation #1 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< #

@login_required(login_url="/loginsystem/")
def insert_file_Solar(request):
    user = auth.get_user(request)
    try:
        file = request.FILES["UserFile"]
        tags = request.POST["Tags"]
        fs = FileSystemStorage()
        # Uploads
        # file_url = "Solar_Rooftop/" + file.name
        # file_fromuser = fs.save(file_url , file)     
        
        SolarRoofTop = SOLARROOFTOP(file=file, tags=tags)
        SolarRoofTop.save()
        
        Who_Action = user
        Action = "Insert File to MOC system"
        Project = "Smart Check Sheet for Substation #1 "
        logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
        logging.save()

        return redirect(request.META['HTTP_REFERER'])
    except:
        return redirect("allproject")

@login_required(login_url="/loginsystem/")  
def DeleteSolarFile(request,id):
    user = auth.get_user(request)
    try:
        SolarRoofTop = SOLARROOFTOP.objects.get(id=id)
        SolarRoofTop.delete()
        
        Who_Action = user
        Action = "Delete Main File From MOC system"
        Project = "Smart Check Sheet for Substation #1 "
        logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
        logging.save()
       
        return redirect(request.META['HTTP_REFERER'])
    except:
       return redirect("allproject")  

@login_required(login_url="/loginsystem/")  
def DeleteSolarFile_Version2(request,id):
    user = auth.get_user(request)
    try:   
        SolarRoofTop = SOLARROOFTOP.objects.get(id=id)
        SolarRoofTop.File_Version2 = "-"
        SolarRoofTop.save()
        
        Who_Action = user
        Action = "Delete File Version 2 From MOC system"
        Project = "Smart Check Sheet for Substation #1 "
        logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
        logging.save()
        
        return redirect(request.META['HTTP_REFERER']) 
    except:
       return redirect("allproject") 
   
@login_required(login_url="/loginsystem/")
def DeleteSolarFile_Version3(request,id):
    user = auth.get_user(request)
    try:
        SolarRoofTop = SOLARROOFTOP.objects.get(id=id)
        SolarRoofTop.File_Version3 = "-"
        SolarRoofTop.save()
        
        Who_Action = user
        Action = "Delete File Version 3 From MOC system"
        Project = "Smart Check Sheet for Substation #1 "
        logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
        logging.save()
        
        return redirect(request.META['HTTP_REFERER']) 
    except:
       return redirect("allproject") 
   
@login_required(login_url="/loginsystem/")  
def DeleteSolarFile_Version4(request,id):
    user = auth.get_user(request)
    try:
        SolarRoofTop = SOLARROOFTOP.objects.get(id=id)
        SolarRoofTop.File_Version4 = "-"
        SolarRoofTop.save()
        
        Who_Action = user
        Action = "Delete File Version 4 From MOC system"
        Project = "Smart Check Sheet for Substation #1 "
        logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
        logging.save()
        
        return redirect(request.META['HTTP_REFERER']) 
    except:
       return redirect("allproject") 
   
@login_required(login_url="/loginsystem/")  
def DeleteSolarFile_Version5(request,id):
    user = auth.get_user(request)
    try:
        SolarRoofTop = SOLARROOFTOP.objects.get(id=id)
        SolarRoofTop.File_Version5 = "-"
        SolarRoofTop.save()
        
        Who_Action = user
        Action = "Delete File Version 5 From MOC system"
        Project = "Smart Check Sheet for Substation #1 "
        logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
        logging.save()
        
        return redirect(request.META['HTTP_REFERER']) 
    except:
       return redirect("allproject") 

@login_required(login_url="/loginsystem/")
def Approve_Solar_File(request,id): # Version1
    user = auth.get_user(request)
    try:
        SolarRoofTop = SOLARROOFTOP.objects.get(id=id)
        SolarRoofTop.status = "Approved"
        SolarRoofTop.save()
        
        Who_Action = user
        Action = "Approve"
        Project = "Smart Check Sheet for Substation #1 "
        logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
        logging.save()
        
        return redirect(request.META['HTTP_REFERER'])
    except:
        return redirect("allproject") 
    
    
def UpdateFileVersion (request,id):
    SolarRoofTop = SOLARROOFTOP.objects.filter(id=id)
    return render(request,"Frontend/UpdateFile.html",{"SolarRoofTop":SolarRoofTop})

def UpdateFileVersion_insert(request,id):
    SolarRoofTop = SOLARROOFTOP.objects.get(id=id)
    user = auth.get_user(request)
    try:
        if SolarRoofTop.File_Version2 == "-":
            File_Version2 = request.FILES["UserFile"]
            SolarRoofTop.File_Version2 = File_Version2
            SolarRoofTop.save()
            
            Who_Action = user
            Action = "Update File Version 2"
            Project = "Smart Check Sheet for Substation #1 "
            logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
            logging.save()
            
        elif SolarRoofTop.File_Version2 != "-" and SolarRoofTop.File_Version3 == "-":
            File_Version3 = request.FILES["UserFile"]
            SolarRoofTop.File_Version3 = File_Version3
            SolarRoofTop.save()
            
            Who_Action = user
            Action = "Update File Version 3"
            Project = "Smart Check Sheet for Substation #1 "
            logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
            logging.save()
            
        elif SolarRoofTop.File_Version2 != "-" and SolarRoofTop.File_Version3 != "-" and SolarRoofTop.File_Version4 == "-":
            File_Version4 = request.FILES["UserFile"]
            SolarRoofTop.File_Version4 = File_Version4
            SolarRoofTop.save()
            
            Who_Action = user
            Action = "Update File Version 4"
            Project = "Smart Check Sheet for Substation #1 "
            logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
            logging.save()
            
        elif SolarRoofTop.File_Version2 != "-" and SolarRoofTop.File_Version3 != "-" and SolarRoofTop.File_Version4 != "-" and SolarRoofTop.File_Version5 == "-":
            File_Version5 = request.FILES["UserFile"]
            SolarRoofTop.File_Version5 = File_Version5
            SolarRoofTop.save()
            
            Who_Action = user
            Action = "Update File Version 5"
            Project = "Smart Check Sheet for Substation #1 "
            logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
            logging.save()
            
        else:
            pass   
        return redirect(request.META['HTTP_REFERER'])
    except:
        return redirect("allproject")
    
    
    
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> As-build drawing P5 package 2 PDF <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< #

@login_required(login_url="/loginsystem/")
def insert_file_Test(request):
    user = auth.get_user(request)
    try:
        file = request.FILES["UserFile"]
        tags = request.POST["Tags"]
        TestProject_EE = PROJECTEE(file=file, tags=tags)
        TestProject_EE.save()
        
        Who_Action = user
        Action = "Insert File to MOC system"
        Project = "As-build drawing P5 package 2 PDF "
        logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
        logging.save()
        
        return redirect(request.META['HTTP_REFERER'])
    except:
        return redirect("allproject")

@login_required(login_url="/loginsystem/")  
def DeleteTestFile(request,id):
    user = auth.get_user(request)
    try:
        TestProject_EE = PROJECTEE.objects.get(id=id)
        TestProject_EE.delete()
        
        Who_Action = user
        Action = "Delete Main File From MOC system"
        Project = "As-build drawing P5 package 2 PDF "
        logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
        logging.save()
        
        return redirect(request.META['HTTP_REFERER']) 
    except:
       return redirect("allproject")  

@login_required(login_url="/loginsystem/")
def Approve_Test_File(request,id):
    user = auth.get_user(request)
    try:
        TestProject_EE = PROJECTEE.objects.get(id=id)
        TestProject_EE.status = "Approved"
        TestProject_EE.save()
        
        Who_Action = user
        Action = "Approve"
        Project = "As-build drawing P5 package 2 PDF "
        logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
        logging.save()
        
        return redirect(request.META['HTTP_REFERER'])
    except:
        return redirect("allproject") 

# def UpdateFileVersion_Test_insert(request,id):
#     TestProject_EE = PROJECTEE.objects.get(id=id)
#     user = auth.get_user(request)
#     try:
#         if TestProject_EE.File_Version2 == "-":
#             File_Version2 = request.FILES["UserFile"]
#             TestProject_EE.File_Version2 = File_Version2
#             TestProject_EE.save()
            
#             Who_Action = user
#             Action = "Update File Version 2"
#             Project = "As-build drawing P5 package 2 PDF"
#             logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
#             logging.save()
            
#         elif TestProject_EE.File_Version2 != "-" and TestProject_EE.File_Version3 == "-":
#             File_Version3 = request.FILES["UserFile"]
#             TestProject_EE.File_Version3 = File_Version3
#             TestProject_EE.save()
            
#             Who_Action = user
#             Action = "Update File Version 3"
#             Project = "As-build drawing P5 package 2 PDF"
#             logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
#             logging.save()
            
#         elif TestProject_EE.File_Version2 != "-" and TestProject_EE.File_Version3 != "-" and TestProject_EE.File_Version4 == "-":
#             File_Version4 = request.FILES["UserFile"]
#             TestProject_EE.File_Version4 = File_Version4
#             TestProject_EE.save()
            
#             Who_Action = user
#             Action = "Update File Version 4"
#             Project = "As-build drawing P5 package 2 PDF"
#             logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
#             logging.save()
            
#         elif TestProject_EE.File_Version2 != "-" and TestProject_EE.File_Version3 != "-" and TestProject_EE.File_Version4 != "-" and TestProject_EE.File_Version5 == "-":
#             File_Version5 = request.FILES["UserFile"]
#             TestProject_EE.File_Version5 = File_Version5
#             TestProject_EE.save()
            
#             Who_Action = user
#             Action = "Update File Version 5"
#             Project = "As-build drawing P5 package 2 PDF"
#             logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
#             logging.save()
            
#         else:
#             pass
#         return redirect(request.META['HTTP_REFERER'])
#     except:
#         return redirect("allproject")

def UpdateFileVersion_Test (request,id):
    TestProject_EE = PROJECTEE.objects.filter(id=id)
    return render(request,"Frontend/UpdateFile_Test.html",{"TestProject_EE":TestProject_EE})

def UpdateFileVersion_insert_Test(request,id):
    TestProject_EE = PROJECTEE.objects.get(id=id)
    user = auth.get_user(request)
    try:
        if TestProject_EE.File_Version2 == "-":
            File_Version2 = request.FILES["UserFile"]
            TestProject_EE.File_Version2 = File_Version2
            TestProject_EE.save()
            
            Who_Action = user
            Action = "Update File Version 2"
            Project = "As-build drawing P5 package 2 PDF"
            logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
            logging.save()
            
        elif TestProject_EE.File_Version2 != "-" and TestProject_EE.File_Version3 == "-":
            File_Version3 = request.FILES["UserFile"]
            TestProject_EE.File_Version3 = File_Version3
            TestProject_EE.save()
            
            Who_Action = user
            Action = "Update File Version 3"
            Project = "As-build drawing P5 package 2 PDF"
            logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
            logging.save()
            
        elif TestProject_EE.File_Version2 != "-" and TestProject_EE.File_Version3 != "-" and TestProject_EE.File_Version4 == "-":
            File_Version4 = request.FILES["UserFile"]
            TestProject_EE.File_Version4 = File_Version4
            TestProject_EE.save()
            
            Who_Action = user
            Action = "Update File Version 4"
            Project = "As-build drawing P5 package 2 PDF"
            logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
            logging.save()
            
        elif TestProject_EE.File_Version2 != "-" and TestProject_EE.File_Version3 != "-" and TestProject_EE.File_Version4 != "-" and TestProject_EE.File_Version5 == "-":
            File_Version5 = request.FILES["UserFile"]
            TestProject_EE.File_Version5 = File_Version5
            TestProject_EE.save()
            
            Who_Action = user
            Action = "Update File Version 5"
            Project = "As-build drawing P5 package 2 PDF"
            logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
            logging.save()
            
        else:
            pass
        return redirect(request.META['HTTP_REFERER'])
    except:
        return redirect("allproject")

@login_required(login_url="/loginsystem/")  
def DeleteTestFile_Version2(request,id):
    user = auth.get_user(request)
    try:
        TestProject_EE = PROJECTEE.objects.get(id=id)
        TestProject_EE.File_Version2 = "-"
        TestProject_EE.save()
        
        Who_Action = user
        Action = "Delete File Version 2 From MOC system"
        Project = "As-build drawing P5 package 2 PDF"
        logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
        logging.save()
        
        return redirect(request.META['HTTP_REFERER']) 
    except:
       return redirect("allproject") 
   
@login_required(login_url="/loginsystem/")  
def DeleteTestFile_Version3(request,id):
    user = auth.get_user(request)
    try:
        TestProject_EE = PROJECTEE.objects.get(id=id)
        TestProject_EE.File_Version3 = "-"
        TestProject_EE.save()
        
        Who_Action = user
        Action = "Delete File Version 3 From MOC system"
        Project = "As-build drawing P5 package 2 PDF"
        logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
        logging.save()
        
        return redirect(request.META['HTTP_REFERER']) 
    except:
       return redirect("allproject") 
   
@login_required(login_url="/loginsystem/")  
def DeleteTestFile_Version4(request,id):
    user = auth.get_user(request)
    try:
        TestProject_EE = PROJECTEE.objects.get(id=id)
        TestProject_EE.File_Version4 = "-"
        TestProject_EE.save()
        
        Who_Action = user
        Action = "Delete File Version 4 From MOC system"
        Project = "As-build drawing P5 package 2 PDF"
        logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
        logging.save()
        
        return redirect(request.META['HTTP_REFERER']) 
    except:
       return redirect("allproject") 
   
@login_required(login_url="/loginsystem/")  
def DeleteTestFile_Version5(request,id):
    user = auth.get_user(request)
    try:
        TestProject_EE = PROJECTEE.objects.get(id=id)
        TestProject_EE.File_Version5 = "-"
        TestProject_EE.save()
        
        Who_Action = user
        Action = "Delete File Version 5 From MOC system"
        Project = "As-build drawing P5 package 2 PDF"
        logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
        logging.save()
        
        return redirect(request.META['HTTP_REFERER']) 
    except:
       return redirect("allproject") 
   

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> DIUDI Improvement<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< #

@login_required(login_url="/loginsystem/")
def insert_file_MLFAULT(request):
    user = auth.get_user(request)
    try:
        file = request.FILES["UserFile"]
        tags = request.POST["Tags"]      
            
        ML_Fault = MLFAULTDETECTION(file=file, tags=tags)
        ML_Fault.save()
        
        Who_Action = user
        Action = "Insert File to MOC system"
        Project = "DIUDI Improvement"
        logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
        logging.save()

        return redirect(request.META['HTTP_REFERER'])
    except:
        return redirect("allproject")

@login_required(login_url="/loginsystem/") 
def DeleteMLFAULTFile(request,id):
    user = auth.get_user(request)
    try:
        ML_Fault = MLFAULTDETECTION.objects.get(id=id)
        ML_Fault.delete()
        
        Who_Action = user
        Action = "Delete Main File From MOC system"
        Project = "DIUDI Improvement"
        logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
        logging.save()
       
        return redirect(request.META['HTTP_REFERER'])
    except:
       return redirect("allproject")  

@login_required(login_url="/loginsystem/")  
def DeleteMLFAULTFile_Version2(request,id):
    user = auth.get_user(request)
    try:   
        ML_Fault = MLFAULTDETECTION.objects.get(id=id)
        ML_Fault.File_Version2 = "-"
        ML_Fault.save()
        
        Who_Action = user
        Action = "Delete File Version 2 From MOC system"
        Project = "DIUDI Improvement"
        logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
        logging.save()
        
        return redirect(request.META['HTTP_REFERER']) 
    except:
       return redirect("allproject") 
   
@login_required(login_url="/loginsystem/")  
def DeleteMLFAULTFile_Version3(request,id):
    user = auth.get_user(request)
    try:
        ML_Fault = MLFAULTDETECTION.objects.get(id=id)
        ML_Fault.File_Version3 = "-"
        ML_Fault.save()
        
        Who_Action = user
        Action = "Delete File Version 3 From MOC system"
        Project = "DIUDI Improvement"
        logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
        logging.save()
        
        return redirect(request.META['HTTP_REFERER']) 
    except:
       return redirect("allproject") 
   
@login_required(login_url="/loginsystem/")  
def DeleteMLFAULTFile_Version4(request,id):
    user = auth.get_user(request)
    try:
        ML_Fault = MLFAULTDETECTION.objects.get(id=id)
        ML_Fault.File_Version4 = "-"
        ML_Fault.save()
        
        Who_Action = user
        Action = "Delete File Version 4 From MOC system"
        Project = "DIUDI Improvement"
        logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
        logging.save()
        
        return redirect(request.META['HTTP_REFERER']) 
    except:
       return redirect("allproject") 
   
@login_required(login_url="/loginsystem/")  
def DeleteMLFAULTFile_Version5(request,id):
    user = auth.get_user(request)
    try:
        ML_Fault = MLFAULTDETECTION.objects.get(id=id)
        ML_Fault.File_Version5 = "-"
        ML_Fault.save()
        
        Who_Action = user
        Action = "Delete File Version 5 From MOC system"
        Project = "DIUDI Improvement"
        logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
        logging.save()
        
        return redirect(request.META['HTTP_REFERER']) 
    except:
       return redirect("allproject") 

@login_required(login_url="/loginsystem/")
def Approve_MLFAULT_File(request,id): # Version1
    user = auth.get_user(request)
    try:
        ML_Fault = MLFAULTDETECTION.objects.get(id=id)
        ML_Fault.status = "Approved"
        ML_Fault.save()
        
        Who_Action = user
        Action = "Approve"
        Project = "DIUDI Improvement"
        logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
        logging.save()
        
        return redirect(request.META['HTTP_REFERER'])
    except:
        return redirect("allproject") 
    
    
def UpdateFileVersion_MLFAULT (request,id):
    ML_Fault = MLFAULTDETECTION.objects.filter(id=id)
    return render(request,"Frontend/UpdateFile_DIUDI.html",{"ML_Fault":ML_Fault})

def UpdateFileVersion_insert_MLFAULT(request,id):
    ML_Fault = MLFAULTDETECTION.objects.get(id=id)
    user = auth.get_user(request)
    try:
        if ML_Fault.File_Version2 == "-":
            File_Version2 = request.FILES["UserFile"]
            ML_Fault.File_Version2 = File_Version2
            ML_Fault.save()
            
            Who_Action = user
            Action = "Update File Version 2"
            Project = "DIUDI Improvement"
            logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
            logging.save()
            
        elif ML_Fault.File_Version2 != "-" and ML_Fault.File_Version3 == "-":
            File_Version3 = request.FILES["UserFile"]
            ML_Fault.File_Version3 = File_Version3
            ML_Fault.save()
            
            Who_Action = user
            Action = "Update File Version 3"
            Project = "DIUDI Improvement"
            logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
            logging.save()
            
        elif ML_Fault.File_Version2 != "-" and ML_Fault.File_Version3 != "-" and ML_Fault.File_Version4 == "-":
            File_Version4 = request.FILES["UserFile"]
            ML_Fault.File_Version4 = File_Version4
            ML_Fault.save()
            
            Who_Action = user
            Action = "Update File Version 4"
            Project = "DIUDI Improvement"
            logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
            logging.save()
            
        elif ML_Fault.File_Version2 != "-" and ML_Fault.File_Version3 != "-" and ML_Fault.File_Version4 != "-" and ML_Fault.File_Version5 == "-":
            File_Version5 = request.FILES["UserFile"]
            ML_Fault.File_Version5 = File_Version5
            ML_Fault.save()
            
            Who_Action = user
            Action = "Update File Version 5"
            Project = "DIUDI Improvement"
            logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
            logging.save()
            
        else:
            pass   
        return redirect(request.META['HTTP_REFERER'])
    except:
        return redirect("allproject")


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Smart Check Sheet for Substation #1 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< #

@login_required(login_url="/loginsystem/")
def insert_file_CheckSheet_Sub1(request):
    user = auth.get_user(request)
    try:
        file = request.FILES["UserFile"]
        tags = request.POST["Tags"]      
            
        CheckSheet_Sub1 = SMARTCHECKSHEETSUBONE(file=file, tags=tags)
        CheckSheet_Sub1.save()
        
        Who_Action = user
        Action = "Insert File to MOC system"
        Project = "Smart Check Sheet for Substation #1"
        logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
        logging.save()

        return redirect(request.META['HTTP_REFERER'])
    except:
        return redirect("allproject")

@login_required(login_url="/loginsystem/") 
def DeleteCheckSheet_Sub1File(request,id):
    user = auth.get_user(request)
    try:
        CheckSheet_Sub1 = SMARTCHECKSHEETSUBONE.objects.get(id=id)
        CheckSheet_Sub1.delete()
        
        Who_Action = user
        Action = "Delete Main File From MOC system"
        Project = "Smart Check Sheet for Substation #1"
        logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
        logging.save()
       
        return redirect(request.META['HTTP_REFERER'])
    except:
       return redirect("allproject")  

@login_required(login_url="/loginsystem/")  
def DeleteCheckSheet_Sub1File_Version2(request,id):
    user = auth.get_user(request)
    try:   
        CheckSheet_Sub1 = SMARTCHECKSHEETSUBONE.objects.get(id=id)
        CheckSheet_Sub1.File_Version2 = "-"
        CheckSheet_Sub1.save()
        
        Who_Action = user
        Action = "Delete File Version 2 From MOC system"
        Project = "Smart Check Sheet for Substation #1"
        logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
        logging.save()
        
        return redirect(request.META['HTTP_REFERER']) 
    except:
       return redirect("allproject") 
   
@login_required(login_url="/loginsystem/")  
def DeleteCheckSheet_Sub1File_Version3(request,id):
    user = auth.get_user(request)
    try:
        CheckSheet_Sub1 = SMARTCHECKSHEETSUBONE.objects.get(id=id)
        CheckSheet_Sub1.File_Version3 = "-"
        CheckSheet_Sub1.save()
        
        Who_Action = user
        Action = "Delete File Version 3 From MOC system"
        Project = "Smart Check Sheet for Substation #1"
        logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
        logging.save()
        
        return redirect(request.META['HTTP_REFERER']) 
    except:
       return redirect("allproject") 
   
@login_required(login_url="/loginsystem/")  
def DeleteCheckSheet_Sub1File_Version4(request,id):
    user = auth.get_user(request)
    try:
        CheckSheet_Sub1 = SMARTCHECKSHEETSUBONE.objects.get(id=id)
        CheckSheet_Sub1.File_Version4 = "-"
        CheckSheet_Sub1.save()
        
        Who_Action = user
        Action = "Delete File Version 4 From MOC system"
        Project = "Smart Check Sheet for Substation #1"
        logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
        logging.save()
        
        return redirect(request.META['HTTP_REFERER']) 
    except:
       return redirect("allproject") 
   
@login_required(login_url="/loginsystem/")  
def DeleteCheckSheet_Sub1File_Version5(request,id):
    user = auth.get_user(request)
    try:
        CheckSheet_Sub1 = SMARTCHECKSHEETSUBONE.objects.get(id=id)
        CheckSheet_Sub1.File_Version5 = "-"
        CheckSheet_Sub1.save()
        
        Who_Action = user
        Action = "Delete File Version 5 From MOC system"
        Project = "Smart Check Sheet for Substation #1"
        logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
        logging.save()
        
        return redirect(request.META['HTTP_REFERER']) 
    except:
       return redirect("allproject") 

@login_required(login_url="/loginsystem/")
def Approve_CheckSheet_Sub1_File(request,id): # Version1
    user = auth.get_user(request)
    try:
        CheckSheet_Sub1 = SMARTCHECKSHEETSUBONE.objects.get(id=id)
        CheckSheet_Sub1.status = "Approved"
        CheckSheet_Sub1.save()
        
        Who_Action = user
        Action = "Approve"
        Project = "Smart Check Sheet for Substation #1"
        logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
        logging.save()
        
        return redirect(request.META['HTTP_REFERER'])
    except:
        return redirect("allproject") 
    
    
def UpdateFileVersion_CheckSheet_Sub1(request,id):
    CheckSheet_Sub1 = SMARTCHECKSHEETSUBONE.objects.filter(id=id)
    return render(request,"Frontend/UpdateFile_Sub1.html",{"CheckSheet_Sub1":CheckSheet_Sub1})

def UpdateFileVersion_insert_CheckSheet_Sub1(request,id):
    CheckSheet_Sub1 = SMARTCHECKSHEETSUBONE.objects.get(id=id)
    user = auth.get_user(request)
    try:
        if CheckSheet_Sub1.File_Version2 == "-":
            File_Version2 = request.FILES["UserFile"]
            CheckSheet_Sub1.File_Version2 = File_Version2
            CheckSheet_Sub1.save()
            
            Who_Action = user
            Action = "Update File Version 2"
            Project = "Smart Check Sheet for Substation #1"
            logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
            logging.save()
            
        elif CheckSheet_Sub1.File_Version2 != "-" and CheckSheet_Sub1.File_Version3 == "-":
            File_Version3 = request.FILES["UserFile"]
            CheckSheet_Sub1.File_Version3 = File_Version3
            CheckSheet_Sub1.save()
            
            Who_Action = user
            Action = "Update File Version 3"
            Project = "Smart Check Sheet for Substation #1"
            logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
            logging.save()
            
        elif CheckSheet_Sub1.File_Version2 != "-" and CheckSheet_Sub1.File_Version3 != "-" and CheckSheet_Sub1.File_Version4 == "-":
            File_Version4 = request.FILES["UserFile"]
            CheckSheet_Sub1.File_Version4 = File_Version4
            CheckSheet_Sub1.save()
            
            Who_Action = user
            Action = "Update File Version 4"
            Project = "Smart Check Sheet for Substation #1"
            logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
            logging.save()
            
        elif CheckSheet_Sub1.File_Version2 != "-" and CheckSheet_Sub1.File_Version3 != "-" and CheckSheet_Sub1.File_Version4 != "-" and CheckSheet_Sub1.File_Version5 == "-":
            File_Version5 = request.FILES["UserFile"]
            CheckSheet_Sub1.File_Version5 = File_Version5
            CheckSheet_Sub1.save()
            
            Who_Action = user
            Action = "Update File Version 5"
            Project = "Smart Check Sheet for Substation #1"
            logging = LOGGING(Who_Action=Who_Action, Action=Action, Project=Project)
            logging.save()
            
        else:
            pass   
        return redirect(request.META['HTTP_REFERER'])
    except:
        return redirect("allproject")