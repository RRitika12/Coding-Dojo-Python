from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout/?$', views.logout),
    url(r'^books$', views.books),
    url(r'^addbook$', views.addbook),
    url(r'^fave/(?P<my_val>\d+)$', views.add_fave),
    url(r'^fav/(?P<my_val>\d+)$', views.add_fav),
    url(r'^unfave/(?P<my_val>\d+)$', views.un_fave),
    url(r'^books/(?P<my_val>\d+)/update$', views.update),
    url(r'^books/(?P<my_val>\d+)$', views.uploaded),
    url(r'^(?P<id>[0-9]+)/delete$',	views.destroy, name="delete_book"),
]