from django.urls import path

from . import views

app_name = 'testBLOG'

urlpatterns = [
    path('', views.post_list, name="post_list"),
    path('tag/<slug:tag_slug>/',views.post_list, name='post_list_by_tag'),
    path('post/<int:pk>', views.post_edit, name='post_edit'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
]