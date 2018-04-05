from django.conf.urls import url


from django.contrib.auth.decorators import login_required #obliga a logearse para acceder a una url
from wlink import views

urlpatterns = [
       
    url(r'^registrar/', login_required(views.registrar), name='registrar'),
    url(r'^registrarCategoria/', login_required(views.registrarCategoria), name='registrarCategoria'),       
    url(r'^eliminar/(?P<id_link>\d+)/$', login_required(views.eliminar), name='eliminar'),    
    url(r'^inicio/', login_required(views.inicio), name='inicio'),
    url(r'$', views.portada, name='portada'),
]
