from django.urls import path
from django.conf.urls import include, url
from django.contrib.staticfiles.urls import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path('', views.base, name='list'),
    path('detail/<int:id>/', views.publicacion_detalle, name='detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()