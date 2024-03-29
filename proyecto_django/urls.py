"""proyecto_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from proyecto_django.views import mi_vista, mostrar_fecha
# otra forma de pedir eso:
from proyecto_django import views


urlpatterns = [
    # path('',mi_vista),
    path ('', views.mi_vista),
    # Pero al hacer eso tambien tenemos que modificar los path
    # path('mostrar-fecha/', mostrar_fecha),
    path('mostrar-fecha/', views.mostrar_fecha),
    path('saludar/<str:nobre>/<str:apellido>', views.saludar),
    path('mi-primer-template/', views.mi_primer_template),
    path('admin/', admin.site.urls),
]
