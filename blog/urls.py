#from django.conf.urls import url
from django.urls import path
from .views import PostList, PostCreate, PostUpdate, PostDelete, PostArchiveYear, PostArchiveMonth, post_detail

urlpatterns = [
       path('create/', PostCreate.as_view(), name='blog_post_create'),
       path('', PostList.as_view(), name='blog_post_list'), # η view είναι class based view
       path('<slug:slug>/', post_detail, name='blog_post_detail'),
       path('<slug:slug>/update', PostUpdate.as_view(), name='blog_post_update'),
       path('<slug:slug>/delete/', PostDelete.as_view(), name='blog_post_delete'),
       path('<year>\d{4}/', PostArchiveYear.as_view(), name='blog_post_archive_year'),
       path('<year>\d{4}/<month>\d{1,2}/', PostArchiveMonth.as_view(), name='blog_post_archive_month'),
       #path('<year>/<month>/<slug:slug>/', post_detail, name='blog_post_detail'),
       #path('', post_list, name='blog_post_list'), # η view είναι function view
       # re_path(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>[-\w]+)/$', post_detail, name='blog_post_detail')
       # re_path(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>[\w\-]+)/$', post_detail, name='blog_post_detail'),
]