from django.shortcuts import render
from pytube import YouTube
from django.http import HttpResponse

# Create your views here.
def home(request):
    if request.method == "POST":
      link = request.POST['link']
      details = YouTube(link)
      video_title = details.title
      return render(request, "base.html",{"title":video_title})
    
    return render(request, "base.html")
    







