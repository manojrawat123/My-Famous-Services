from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from services.views import ServiceApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('services/', ServiceApiView.as_view(), name="service"),
    path('services/<slug:slug>/', ServiceApiView.as_view(), name="")
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
