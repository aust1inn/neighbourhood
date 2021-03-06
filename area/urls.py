from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^createhood/$', views.create_hood, name='create_hood'),
    url(r'^join/(\d+)', views.join, name='join'),
    url(r'^search/$', views.search, name='search'),
    url(r'^exitHood/(\d+)', views.exitHood, name='exitHood'),
    url(r'^createpost/$', views.create_post, name='create_post'),
    url(r'^new/business', views.new_business, name='add_business'),
    url(r'^deletepost/(\d+)', views.delete_post, name='delete_post'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
