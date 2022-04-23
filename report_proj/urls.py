from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = 'Global Reports Administration'
admin.site.site_title = 'Global Reports Site'
admin.site.index_title= 'Global Reports Models'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sales.urls', namespace='sales')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
