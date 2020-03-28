from django.contrib import admin
from django.urls import path
from predict import views
from django.views.generic import View,TemplateView
app_name='predict'

urlpatterns=[
    path('',TemplateView.as_view(template_name='predict/predict.html')),
    path('post',views.post,name='post'),
    
]