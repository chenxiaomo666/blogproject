from django.urls import path 
from . import views 

# 视图函数命名空间
app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:pk>', views.detail, name='detail')
]
