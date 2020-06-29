from django.urls import path
from . import views

urlpatterns=[
    path('dashboard', views.dashboard, name='dashboard'),
    path('production_table', views.production_table, name='production_table'),
    path('transport_table', views.transport_table, name='transport_table'),
]