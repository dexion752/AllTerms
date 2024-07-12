from django.urls import path
from config import views
# from models import southIndex
from .views import base_views
app_name = 'south'

urlpatterns = [
    path('', base_views.indexTest, name='index'),
    # path('', )
    path('astro/', base_views.astroList, name='astroList'),
    path('biochemi/', base_views.biochemiList, name='biochemi'),

]