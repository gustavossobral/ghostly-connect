from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('usuario.urls')),
    path('', include('home.urls')),
    path('postagens/', include('postagens.urls')),
    path('reports/', include('reports.urls'))
]
