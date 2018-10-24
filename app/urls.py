from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    url(r'^$', views.index), # root
    url(r'^login$', views.login_view), # login
    url(r'^logout$', views.logout_view), # logout
    url(r'^signup$', views.signup), # signup
    url( r'^ribbits$' , views.public ) ,  # public ribbits
    url( r'^submit$' , views.submit ) ,  # submit new ribbit
]
if settings.DEBUG:
    urlpatterns+=static( settings.MEDIA_URL , document_root=settings.MEDIA_ROOT )
