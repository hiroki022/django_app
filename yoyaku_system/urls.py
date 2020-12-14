from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('yoyaku',views.yoyaku, name='yoyaku'),
    path('confirm', views.confirm, name='confirm'),
    #path('edit/<int:num>',views.edit,name='edit'),
]