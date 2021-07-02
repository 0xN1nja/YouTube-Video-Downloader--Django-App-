from django.http import HttpResponse
from django.shortcuts import render
from pytube import YouTube
from pathlib import Path
import os
def index(request):
    return render(request,"index.html")
def analyze_to_mp3(request):
    link=request.POST.get("link")
    try:
        yt=YouTube(link)
        ys=yt.streams.get_by_itag("140")
        BASE_DIR = Path(__file__).resolve().parent.parent
        ys.download(BASE_DIR)
        params={"status":"Successfully Downloaded !","location":f"{os.path.join(BASE_DIR,yt.title)}.mp3","Format":"MP3","Title":yt.title,"Description":yt.description,"Rating":yt.rating,"Duration":yt.length}
    except:
        return HttpResponse("<h1>403<br>Please Enter A Valid URL</h1>")
    return render(request,"analyze_to_mp3.html",params)
def analyze_to_mp4(request):
    link=request.POST.get("link")
    print(link)
    try:
        yt=YouTube(link)
        ys=yt.streams.get_by_itag("22")
        BASE_DIR = Path(__file__).resolve().parent.parent
        ys.download(BASE_DIR)
        params={"status":"Successfully Downloaded !","location":f"{os.path.join(BASE_DIR,yt.title)}.mp4","Format":"MP4","Title":yt.title,"Description":yt.description,"Rating":yt.rating,"Duration":yt.length}
    except:
        return HttpResponse("<h1>403<br>Please Enter A Valid URL</h1>")
    return render(request,"analyze_to_mp4.html",params)