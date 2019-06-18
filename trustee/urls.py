from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^contact-us/$', views.contact, name='contact'),
    url(r'^online-quiz/$', views.quiz, name='quiz'),
    url(r'^tution-11&12th/$', views.tution, name='tution'),
    url(r'^about-us/$', views.about, name='about'),
    url(r'^Uqaab-trust/$', views.uqaab, name='uqaab'),
    url(r'^leadership-team/$', views.leadership, name='leadership'),
    url(r'^support-team/$', views.support, name='support'),
    url(r'^faculty-team/$', views.faculty, name='faculty'),
    url(r'^Uqaab-trust-donate/$', views.donate, name='donate'),
    url(r'^Madrasa-Parvaz-ul-Uloom/$', views.madrasa, name='madrasa'),
]