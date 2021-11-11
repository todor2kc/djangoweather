#this is important
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'), #kada promenim iz about.html u about sve pukne ali kad kliknem prvo na weather pa onda na abput ono krene da radi

]

