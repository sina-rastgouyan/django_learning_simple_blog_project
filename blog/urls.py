from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog_home'),
    # path('', views.blog_home_view, name='blog_home'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    # path('<int:pk>/', views.post_detail_view, name='post_detail'),
    path('new_post/', views.PostCreateView.as_view(), name='new_post'),
    # path('new_post/', views.new_post_view, name='new_post'),
    path('<int:pk>/edit/', views.PostUpdateView.as_view(), name='edit_post'),
    # path('<int:pk>/edit/', views.edit_post_view, name='edit_post'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete_post')
    # path('<int:pk>/delete/', views.delete_post_view, name='delete_post')
]
