from django.conf.urls import url
from . import views

app_name = 'pages'
urlpatterns = [
    # /pages/work/
    url(r'^work/$', views.WorkView.as_view(), name='work'),
    # /pages/work/#/
    url(r'^work/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='details'),
    # /pages/projects/
    url(r'^projects/$', views.ProjectView.as_view(), name='projects'),
    # /pages/projects/#/
    url(r'^projects/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='details'),
    # /pages/aboutMe/
    url(r'^aboutMe/$', views.aboutMe, name='aboutMe'),

    # /pages/test/listview/
    url(r'^test/listview/$', views.TestListView.as_view(), name='test_list'),
    # /pages/test/detailview/
    url(r'^test/detailview/$', views.TestDetailView.as_view(), name='test_detail')
]
