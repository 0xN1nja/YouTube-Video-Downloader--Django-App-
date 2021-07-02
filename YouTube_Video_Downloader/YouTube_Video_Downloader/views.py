from django.http import HttpResponse
from django.shortcuts import render
from pytube import YouTube
from pathlib import Path
import os
ys=None
def index(request):
    return render(request,"index.html")
def analyze_to_mp3(request):
    global ys
    link=request.POST.get("link")
    try:
        yt=YouTube(link)
        ys=yt.streams.get_by_itag("140")
        BASE_DIR = Path(__file__).resolve().parent.parent
        params={"img":yt.thumbnail_url,"status":"Successfully Downloaded !","location":f"{os.path.join(BASE_DIR,yt.title)}.mp3","Format":"MP3","Title":yt.title,"Description":yt.description,"Rating":f"{yt.rating}","Duration":f"{yt.length} Seconds"}
    except:
        return HttpResponse("<h1>403<br>Please Enter A Valid URL</h1>")
    return render(request,"analyze_to_mp3.html",params)
def analyze_to_mp4(request):
    global ys
    link=request.POST.get("link")
    try:
        yt=YouTube(link)
        ys=yt.streams.get_by_itag("22")
        BASE_DIR = Path(__file__).resolve().parent.parent
        params={"status":"Successfully Downloaded !","location":f"{os.path.join(BASE_DIR,yt.title)}.mp4","Format":"MP4","Title":yt.title,"Description":yt.description,"Rating":f"{yt.rating}","Duration":f"{yt.length} Seconds"}
    except:
        return HttpResponse("<h1>403<br>Please Enter A Valid URL</h1>")
    return render(request,"analyze_to_mp4.html",params)
def download(request):
    ys.download()
    return HttpResponse("<h1>Downloaded Successfully</h1>")