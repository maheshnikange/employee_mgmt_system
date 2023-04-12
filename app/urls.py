
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('',views.index,name='index' ),
    path('allemp/',views.allemp,name='allemp' ),
    path('addemp',views.addemp,name='addemp' ),
    path('removeemp/<int:emp_id>',views.removeemp,name='removeemp1' ),
    path('removeemp/',views.removeemp,name='removeemp2' ),


]