from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('apps.measures.urls')),
    path('api/v1/', include('apps.accounts.urls')),
    path('api/v1/', include('apps.raspberry.urls')),
    path('', include('apps.information.urls')),
]
