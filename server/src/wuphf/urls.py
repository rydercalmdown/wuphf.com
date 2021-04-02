"""wuphf URL Configuration"""

from django.contrib import admin
from django.urls import path
from wuphf import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name='home'),
    path('sent', views.WuphfSent.as_view(), name='wuphf_sent'),
    path('api/list/', views.WuphfMessagesList.as_view()),
    path('api/details/', views.WuphfMessagesDetails.as_view()),
]
