from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url('^$',views.photos,name = 'photos'),
    url(r'^search/', views.search_results,name='search_results'),
    url(r'^photo/(\d+)',views.singlephoto, name='singlephoto'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
