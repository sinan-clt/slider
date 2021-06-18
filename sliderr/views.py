from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def slider(request):
  return render(request,'slider.html')

  