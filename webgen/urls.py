from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.html_list, name='html_list')
]
