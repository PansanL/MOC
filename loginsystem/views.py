from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User, auth  # เข้าถึง auth_user Table
from django.contrib.auth.decorators import login_required # การบังครับ login
from django.contrib.auth.models import auth, User

# Create your views here.
def index(request):
    return render(request,"Frontend/login.html")

def register(request):
    if request.method == "POST" :
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        if username == "" or email == "" or password == "" or repassword == "":
            messages.info(request,"กรุณาป้อนข้อมูลให้ครบ")
            return redirect("/loginsystem")
        
        else:
            if password == repassword:
                if User.objects.filter(username=username).exists():
                    messages.info(request,"Username นี้มีคนใช้แล้ว")
                    return redirect("/loginsystem")
                elif User.objects.filter(email=email).exists():
                    messages.info(request,"Email นี้เคยลงทะเบียบแล้ว")
                    return redirect("/loginsystem")
                else:
                    user = User.objects.create_user(
                    username = username,
                    email = email,
                    password = password
                )
                    user.save()
                    messages.info(request,"สร้างบัญชีเรียบร้อยแล้ว")
                    return redirect("/loginsystem")

            else:
                messages.info(request,"ไม่สามารถลงทะเบียนได้เนื่องจากรหัวผ่านไม่ตรงกัน")
                return redirect("/loginsystem")


        
def mainProgram(request):  # Login
    username = request.POST["username"]  # เมื่อพิม 1000288663 ก็จะเก็บไว้ในตัวแปร password
    password = request.POST["password"]
    user = auth.authenticate(username=username,password=password) # รับ request เข้ามาทำงาน เพื่อมา check ว่ามีข้อมูลใน DB หรือป่าว
    if user is not None:
        auth.login(request,user)
        return redirect("panel")
    else:
        messages.info(request,"ไม่พบข้อมูลบัญชีผู้ใช้")
        return redirect("/loginsystem")

def logout(request):
    auth.logout(request)
    return redirect('/loginsystem')



# def login(request):
#     username = request.POST["username"]  # เมื่อพิม 1000288663 ก็จะเก็บไว้ในตัวแปร password
#     password = request.POST["password"]  
#     user = auth.authenticate(username=username,password=password) # รับ request เข้ามาทำงาน เพื่อมา check ว่ามีข้อมูลใน DB หรือป่าว
#     if user is not None:
#         auth.login(request,user)
#         return redirect ("")
        
#     else:
#         messages.info(request,"ไม่พบข้อมูลบัญชีผู้ใช้")