from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^contact-us/$', views.contact, name='contact'),
    url(r'^online-quiz/$', views.quiz, name='quiz'),
    url(r'^tution-11&12th/$', views.tution, name='tution'),
]