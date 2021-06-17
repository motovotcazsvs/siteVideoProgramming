from django.shortcuts import render, redirect
from .models import videoSite
from .forms import videoForm


def home(request):
    obj = videoSite.objects.all()   
    return render(request, 'appVideoProgramming/home.html', {'obj' : obj})

def userVideo(request):
    if request.method == 'POST':
        form = videoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = videoForm() 
    return render(request, 'appVideoProgramming/userVideo.html', {'form' : form})



