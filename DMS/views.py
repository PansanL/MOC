from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from registernewproject.models import REGISTERNEWPROJECT
from django.core.files.storage import FileSystemStorage
# Create your views here.

@login_required(login_url="/loginsystem/")
def panel(request):
    registernewproject = REGISTERNEWPROJECT.objects.all()
    return render(request,"Frontend/mainProgram.html",{"registernewproject":registernewproject})


    