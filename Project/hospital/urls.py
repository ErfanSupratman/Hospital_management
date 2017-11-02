from django.conf.urls import include, url
from . import views
from django.contrib.auth.views import password_reset, password_reset_done

urlpatterns = [
    url(r'^$',views.home, name='home'),
    url(r'^login/$',views.login, name='login'),
    url(r'^signup/$',views.signup, name='signup'),
    url(r'^appointment/$',views.appointment, name='appointment'),
    #url(r'^change_password/$',password_reset),
    #url(r'^password_reset_done/$',password_reset_done),
    url(r'^forgetpassword/$',views.forgetpassword, name='forgetpassword'),
]