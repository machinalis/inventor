from django.conf.urls import patterns, url
from stock import views

urlpatterns = patterns('',
    url(r'uncontained_parts$', views.UncontainedPartsView.as_view(),
        name='uncontained_parts'),
)