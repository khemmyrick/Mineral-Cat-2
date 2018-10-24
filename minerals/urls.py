from django.urls import path

from . import views

app_name = 'minerals'
urlpatterns = [
    path('', views.index, name='index'),
    path('mineral_list/', views.mineral_list, name='mineral_list'),
    path('random_mineral/', views.random_mineral, name='random_mineral'),
    path('random_group/', views.random_group, name='random_group'),
    path('mineral_detail/<pk>/', views.mineral_detail, name='mineral_detail'),
    path('group_list/<pk>', views.group_list, name='group_list'),
    path('by_alpha/<term>', views.by_alpha, name='by_alpha'),
    path('search/', views.search, name='search'),
    path('random_ingroup/<pk>', views.random_ingroup, name='random_ingroup'),
]
