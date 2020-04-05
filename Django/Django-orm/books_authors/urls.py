from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.main),
    url(r'^authors$', views.authors),
    url(r'^book/(?P<my_val>\d+)$', views.onebook),
    url(r'^author/(?P<my_val>\d+)$', views.oneauthor),
    url(r'^addbook$', views.addbook),
    url(r'^addauthor$', views.addauthor),
    url(r'^getbook/(?P<my_val>\d+)$', views.getbook),
    url(r'^getauthor/(?P<my_val>\d+)$', views.getauthor),
]