from django.shortcuts import render
from .models import Photo
from django.http import HttpResponse

# Create your views here.
def test(request):
    return render(request,'welcome.html')

def photos(request):
    photos = Photo.display_photos()
    return render(request, 'photos.html',{"photos":photos})
