from django.conf.urls import url
from . import views

app_name = 'pages'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^work/$', views.WorkView.as_view(), name='work'),
    url(r'^projects/$', views.ProjectView.as_view(), name='projects'),
    url(r'^aboutMe/$', views.aboutMe, name='aboutMe'),
    url(r'^details(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='details')
]
