from django.contrib import admin
from django.urls import path
from A.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login_page/',login_page,name="login_page"),
    path('logout_page/',logout_page,name="logout_page"),
    path('',home),
    path('house/',house),
    path('car/',car,name="car"),
    path('delete-car/<id>/',delete_car,name = "delete_car"),
    path('update_car/<id>/',update_car,name = "update_car"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()