from django.http import HttpResponse
from django.shortcuts import render
from pytube import YouTube
def index(request):
    return render(request,"index.html")
def analyze_to_mp3(request):
    link=request.POST.get("link")
    try:
        yt=YouTube(link)
    except:
        return HttpResponse("<h1>403<br>Please Enter A Valid URL</h1>")
    return render(request,"analyze.html")
def analyze_to_mp4(request):
    pass