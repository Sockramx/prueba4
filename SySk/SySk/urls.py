"""SySk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib.auth.views import login, logout_then_login
from django.contrib.auth.decorators import login_required
from wlink import views
from django.contrib import admin



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^wlink/', include('wlink.urls', namespace="wlink")), 
    url(r'^accounts/login', login, {'template_name':'login.html'}, name="login"),
    url(r'^accounts/profile', login_required(views.perfil), name="perfil"),
    url(r'^accounts/logout', logout_then_login, name="logout"),    
    url(r'^registrar/', login_required(views.registrar), name='registrar'),
    url(r'^registrarCategoria/', login_required(views.registrarCategoria), name='registrarCategoria'),       
    url(r'^eliminar/(?P<id_link>\d+)/$', login_required(views.eliminar), name='eliminar'),    
    url(r'^inicio/', login_required(views.inicio), name='inicio'),
    url(r'$', views.portada, name='portada'),
]
