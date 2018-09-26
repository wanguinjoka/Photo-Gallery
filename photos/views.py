from django.shortcuts import render
from .models import Photo
from django.http import HttpResponse

# Create your views here.
def test(request):
    return render(request,'welcome.html')

def photos(request):
    photos = Photo.display_photos()
    return render(request, 'photos.html',{"photos":photos})

def search_results(request):

    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_photos = Photo.search_by_category(search_term)

        message = f"{search_term}"

        return render(request, 'search.html',{"message":message, "photos": searched_photos})

    else:
        message ="Search according to: Career,Travel,Family,Hobbies"

        return render(request,'search.html',{"message":message})

def singlephoto(request,photo_id):
    try:
        singlephoto = Photo.objects.get(id = photo_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"singlephoto.html",{"singlephoto":singlephoto})
