from django.urls import path
from . import views
from django.conf.urls import url
# from blog.views import add_like, add_dislike
# app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^blogs/$', views.BlogListView.as_view(), name='blogs'),
    url(r'^blog-detail/(?P<pk>\d+)$', views.BlogDetailView.as_view(), name='blog-detail'),
    url(r'^blogers/$', views.BlogerListView.as_view(), name='blogers'),
    url(r'^bloger/(?P<pk>\d+)$', views.BlogerDetailView.as_view(), name='bloger-detail'),
    url(r'^comment/like/(?P<pk>\d+)$', views.CommentLikeView.as_view(), name='likes'),
]

urlpatterns += [
    url(r'^comment/create/(?P<pk>\d+)$', views.CommentCreate.as_view(), name='comment_create'),

]

