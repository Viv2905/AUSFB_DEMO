from django.urls import path
from . import views
# from app_api import views

urlpatterns = [
    path('data/', views.database.as_view()),
    path('cus-login/', views.customer),
    path('cus-login/cus-record/', views.customer),
    path("adm-login/", views.admin1),
    path("adm-login/adm-record/", views.admin1),
    path("pushdata/", views.push),
    path('', views.front)
]