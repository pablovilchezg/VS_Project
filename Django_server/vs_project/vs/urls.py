# WGG this file contains urls specific to the vs project
from django.conf.urls import patterns, url
from vs import views
from django.views.generic import RedirectView

# WGG this tuple must be called urlpatterns for django to
# pick it up. ^$ matches an empty string, in this example
# http://www.tangowithdjango.com/vs/ is considered blank
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name="login"),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^geolocate/$', views.poi_list, name='geolocate'),
    url(r'^activarlocalizacion/$', views.activarlocalizacion, name='activarlocalizacion'),
    url(r'^desactivarlocalizacion/$', views.desactivarlocalizacion, name='desactivarlocalizacion'),
    url(r'^introducirlocalizacion/$', views.introducirlocalizacion, name='introducirlocalizacion'),
    url(r'^borrarhistorialub/$', views.borrarhistorialub, name='borrarhistorialub'),
    url(r'^camera/$', views.camera, name='camera'),
    url(r'^activarcamara/$', views.activarcamara, name='activarcamara'),
    url(r'^desactivarcamara/$', views.desactivarcamara, name='desactivarcamara'),
    url(r'^directorio$', views.directorio, name='directory_index'),
    url(r'^list/$', views.list_directory, name='directory_list'),
    url(r'^list_directories/(?P<path>.*)/(?P<directorio>.*)/$', views.list_directories, name='directories_list'),
    url(r'^download-file/(?P<path>.*)/(?P<file_name>.*)/$', views.download_file, name='directory_download_file'),
    url(r'^borrarhistorialint/$', views.borrarhistorialint, name='borrarhistorialint'),
    url(r'^activarAP/$', views.activarAP, name='activarAP'),
    url(r'^desactivarAP/$', views.desactivarAP, name='desactivarAP'),
)

