from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/results/
    url(r'^(?P<weapon_id>[0-9]+)/results/$', views.results, name='results')
]