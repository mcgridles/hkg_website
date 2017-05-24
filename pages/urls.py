from django.conf.urls import url

from . import views

app_name = 'pages'
urlpatterns = [
    # /pages/work/
    url(r'^work/$', views.ListView.as_view(), name='work'),
    # /pages/work/<pk>/
    url(r'^work/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='details'),
]
