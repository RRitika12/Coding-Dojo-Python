from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^shows$', views.shows),
    url(r'^addnew$', views.addnew),
    url(r'^shows/new$', views.shows_new),
    url(r'^shows/(?P<my_val>\d+)/edit$', views.shows_edit),
    url(r'^shows/(?P<my_val>\d+)/edit/process$', views.process_edit),
    url(r'^shows/(?P<my_val>\d+)$', views.show_one, name="show_one"),
    url(r'^(?P<id>[0-9]+)/delete$',	views.destroy, name="delete_show"),
    
]
