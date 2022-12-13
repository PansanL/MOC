from django.urls import path
from .views import index,register,mainProgram,logout

urlpatterns = [
    path('',index),
    path('register/add',register,name="addUser"),
    path('mainProgram/',mainProgram,name="mainProgram"),  # เอา name = "login" ไปใส่ใน action ของแบบ form
    path('logout/',logout,name="logout"),
]
