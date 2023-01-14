from django.urls import path
from django.conf import Settings
from .views import home
urlpatterns = [
   path('', home), 
]
# if Settings.DEBUG:
#    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.   MEDIA_ROOT)
