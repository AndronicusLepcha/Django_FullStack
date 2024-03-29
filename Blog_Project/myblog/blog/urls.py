from django.conf.urls import url
from blog import views

urlpatterns=[
    path('about/',views.AboutView().as_view(),name='about'),
    path('',views.PostListView(),name='post_list'),
    path('post/(?P<pk>\d+)',views.PostDetialView.as_view(),name='post_detail'),
    path('post/new/',views.CreatePostView.as_view(),name='post_new'),
    path('post/(?P<pk>\d+)/edit/',views.PostUpdateView.as_view(),name='post_edit'),
    path('post/(?P<pk>\d+)/remove/',views.PostDeleteView.as_view(),name='post_remove'),
    path('drafts/',views.DraftListView.as_view(),name='post_draft_list'),
]