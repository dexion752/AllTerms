
from django.urls import path
from config import views
from models import southIndex
app_name = 'south'

urlpatterns = [
    path('', views.indexTest),
    path('astro/', ),
]