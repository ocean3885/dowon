from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('base.urls')),
    path('m/', include('mobile.urls')),
    path('manseryuk/', include('manseryuk.urls')),
]
