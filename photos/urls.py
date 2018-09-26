from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url('^$',views.photos,name = 'photos'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
