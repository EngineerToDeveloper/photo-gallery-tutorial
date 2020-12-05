from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from pages.views import add_pet_view, gallery_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pet/<int:pk>/', gallery_view, name="index"),
    path('addpet/', add_pet_view, name="add_pet"),
]

if settings.DEBUG:
    urlpatterns  += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns  += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
