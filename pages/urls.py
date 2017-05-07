from django.conf.urls import url

from . import views

app_name = 'pages'
urlpatterns = [
    # /pages/work/
    url(r'^work/$', views.WorkView.as_view(), name='work'),
    # /pages/work/<pk>/
    url(r'^work/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='work_details'),
    # /pages/projects/
    url(r'^projects/$', views.ProjectView.as_view(), name='projects'),
    # /pages/projects/<pk>/
    url(r'^projects/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='project_details'),
]
