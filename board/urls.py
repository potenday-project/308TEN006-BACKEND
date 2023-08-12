from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.post, name='post'),
    path('<int:memo_id>/', views.detail, name='detail'),
    path('like/', views.like, name='like'),
    path('<int:memokey>/comment_write/', views.comment_write, name='comment_write'),
    path('<int:memo_pk>/<int:pk>/comment_delete/', views.comment_delete, name='comment_delete'),
    path('category/<str:category_name>/', views.category, name='category'),

    ### 하나씩 살리기 ~ ###
    # path('<int:memokey>/modify/', views.modify, name='modify_memo'),
    # path('<int:memokey>/delete/', views.delete, name='delete_memo'),
    path('explore/tags/<str:tag>/', views.index, name='post_search'),
    # path('search/', views.search, name='search'),
    ###
]
