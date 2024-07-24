from django.urls import path
from config import views
# from models import southIndex
from .views import base_views
app_name = 'south'

urlpatterns = [
    # path('', base_views.indexTest, name='index'),
    path('', base_views.srcList, name='srcIndex'),
    # path('', )
    path('nastro/', base_views.nAstroList, name='nastro'),
    path('nbiochemi/', base_views.nBiochemiList, name='nbiochemi'),
    path('nbotany/', base_views.nBotanyList, name='nbotany'),
    path('nbuddh/', base_views.nBuddhList, name='nbuddh'),
    path('ncell/', base_views.nCellList, name='ncell'),
    path('nchemi/', base_views.nChemiList, name='nchemi'),
    path('nlife/', base_views.nLifeList, name='nlife'),
    path('nchemipedia/', base_views.nChemiPediaList, name='nchemipedia'),
    path('nmath/', base_views.nMathList, name='nmath'),

]