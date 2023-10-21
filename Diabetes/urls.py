from django.contrib import admin
from django.urls import path,include

import usersauth
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name="home"),
    path('',include('usersauth.urls')),
    path('result/',views.result,name="result"),
    path('details/',views.report,name="details"),
    
]
