from django.urls import path
from . import views


app_name = 'bills'
urlpatterns = [
    path('', views.index, name='index'),
    path('bill_list', views.bill_list, name='bill_list'),
    path('bill/<int:pk>', views.bill_detail, name='bill_detail'),
    path('bill/<int:pk>/prev', views.bill_detail_prev, name='bill_detail_prev'),
    path('bill/<int:pk>/next', views.bill_detail_next, name='bill_detail_next'),
    path('bill/<int:pk>/edit', views.bill_edit, name='bill_edit'),
    path('bill/<int:pk>/delivered', views.bill_delivered, name='bill_delivered'),
    path('bill/new', views.bill_new, name='bill_new'),


    path('test/', views.test, name='test'),
    # path('test2/', views.test2, name='test2'),
    # path('test3/', views.test3, name='test3'),

]
