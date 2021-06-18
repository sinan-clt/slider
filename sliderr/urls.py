from django.urls import path,include
from . import views

urlpatterns = [
    path('slider',views.slider,name='slider'),
    
]
