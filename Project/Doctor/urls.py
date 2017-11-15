from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^doc_login/$', views.Doctor_login, name='login'),
    url(r'^doc_signup/$', views.Doctor_SignUp, name='signup'),
]
