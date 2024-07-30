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
    path('nmeteo/', base_views.nMeteoList, name='nmeteo'),
    path('nearth/', base_views.nEarthList, name='nearth'),
    path('ngeo/', base_views.nGeoList, name='ngeo'),
    path('nocean/', base_views.nOceanList, name='nocean'),
    path('nzoo/', base_views.nZooList, name='nzoo'),
    path('nmicrobio/', base_views.nMicroBioList, name='nmicrobio'),
    path('nfood/', base_views.nFoodList, name='nfood'),
    path('nwater/', base_views.nWaterList, name='nwater'),
    path('nmine/', base_views.nMineList, name='nmine'),
    path('nweather/', base_views.nWeatherList, name='nweather'),
    path('ngovern/', base_views.nGovernList, name='ngovern'),

]