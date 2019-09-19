from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('add/', views.add_wish, name='add_wish'),
    path('<int:id>/', views.drop_wish, name='drop_wish')
]
