from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib import admin

from . import views #resultpage,frontpage,index,ContactFormView

app_name = 'QRer'

urlpatterns = [
    path('result/', views.resultpage, name='result'),
    path('', views.frontpage, name='frontpage'),
    path('main/', views.index, name='index'),
    path('maker/', views.maker, name='maker'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('contact/result', views.ContactResultView.as_view(), name='contact_result'),
    path('accounts/', include('accounts.urls')),
    path('accounts/logout', views.logout_view),
    path('accounts/', include('django.contrib.auth.urls')),
]