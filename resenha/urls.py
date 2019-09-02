import resenhando
from resenhando import admin
from django.contrib import admin
from django.urls import path, include
from resenhando import views

urlpatterns = [
    path('',include('resenhando.urls')), 
    path('lista_filmes/', include('resenhando.urls')),
    path('admin/', admin.site.urls),  
]
