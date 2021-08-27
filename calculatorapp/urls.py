
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index1'),
    path('submitquery',views.submitquery,name='submitquery'),
    
]
