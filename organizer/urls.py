from django.urls import path
from .views import (StartupDetail, StartupList, TagCreate, TagUpdate, TagDelete, StartupCreate, StartupUpdate, StartupDelete, NewsLinkCreate, NewsLinkUpdate, NewsLinkDelete, TagDetail, TagList, TagPageList)

urlpatterns = [
    # path('', homepage),
    #path('tag/<slug>[\w\-]+/', tag_detail, name='organizer_tag_detail'),
    path('tag/', TagList.as_view(), name='organizer_tag_list'),
    path('tag/<page_number>\d+/', TagPageList.as_view(), name='organizer_tag_page'),
    path('tag/create/', TagCreate.as_view() , name='organizer_tag_create'),
    path('tag/<slug:slug>/', TagDetail.as_view(), name='organizer_tag_detail'),
    path('tag/<slug:slug>/update/', TagUpdate.as_view(), name='organizer_tag_update'),
    path('tag/<slug:slug>/delete/', TagDelete.as_view(), name='organizer_tag_delete'),
    path('startup/', StartupList.as_view(), name='organizer_startup_list'),
    path('startup/create/', StartupCreate.as_view(), name='organizer_startup_create'),
    path('startup/<slug:slug>/', StartupDetail.as_view(), name='organizer_startup_detail'),
    path('startup/<slug:slug>/update/', StartupUpdate.as_view(), name='organizer_startup_update'),
    path('startup/<slug:slug>/delete/', StartupDelete.as_view(), name='organizer_startup_delete'),
    path('newslink/create/', NewsLinkCreate.as_view(), name='organizer_newslink_create'),
    path('newslink/update/<pk>\d/', NewsLinkUpdate.as_view(), name='organizer_newslink_update'), 
    path('newslink/delete/<pk>\d/', NewsLinkDelete.as_view(), name='organizer_newslink_delete'),   
]
