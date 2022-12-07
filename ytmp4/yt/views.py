from django.shortcuts import render
from pytube import YouTube
from django.http import HttpResponse

# Create your views here.
def home(request):
    if request.method == "POST":
      link = request.POST['link']
      print(link)
      return render(request, "base.html")
    
    return render(request, "base.html")
    







