from django.urls import path
from .views import panel

from django.contrib.auth.decorators import login_required # การบังครับ login
urlpatterns = [
    path('',panel,name="panel"),

]