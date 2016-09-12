from django.conf.urls import url
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="webgen/index.html"), name='main_page'),
    url(r'^list$', views.html_list, name='html_list'),
    url(r'^dashboard', views.dashboard, name='dashboard'),
]
