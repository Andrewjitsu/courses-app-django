from django.conf.urls import url
from . import views           
  # ^ So we can call functions from our routes!
urlpatterns = [
 url(r'^$', views.index),
 url(r'^new_course$', views.create),
 url(r'^confirm/(?P<id>\d+)$', views.confirm),
 url(r'^courses/destroy/(?P<id>\d+)$', views.destroy, name="destroy")       
]
  