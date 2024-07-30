from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from ..models import Sources, NaverAstro, NaverBiochemi, NaverBotany, NaverBuddh, NaverCell, NaverChemi, NaverLife, NaverChemiPedia, NaverMath, NaverMeteo, NaverEarth, NaverGeo, NaverOcean
from ..models import *

from django.db.models import Q

# Create your views here.

def indexTest(request):
    return HttpResponse("urls.py와 base_views.py 연동을 테스트 중입니다.")

def srcList(request):
    MAX_LIST_CNT = 10
    last_page_num = 0
    total_s = 0
    total_n = 0
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    terms_list = Sources.objects.order_by('id')
    s_list = terms_list.filter(code='s')
    n_list = terms_list.filter(code='n')
    for no in range(terms_list.count()):
        row = terms_list.get(id=no)
        if row.code == 's':
            total_s = total_s + row.sum
        else:
            total_n = total_n + row.sum
    cnt = Sources.objects.count()
    if kw:
        terms_list = terms_list.filter(
            Q(title__icontains=kw)  |
            # Q(simple_sense__icontains=kw) |
            Q(code__icontains=kw)
        ).distinct()
        cnt = terms_list.count()
    paginator = Paginator(terms_list, MAX_LIST_CNT)
    for page_num in paginator.page_range:
        last_page_num = last_page_num + 1
    last_page_num = last_page_num + 1
    page_obj = paginator.get_page(page)
    context = {'terms_list' : page_obj,
               'last_page_num' : last_page_num,
               'page' : page,
               'kw' : kw,
               'cnt' : cnt,
               'total_n' : total_n,
               'total_s' : total_s,
               }
    return render(request, 'southterms/terms_sources_list.html', context)

def nAstroList(request):
    MAX_LIST_CNT = 10
    last_page_num = 0
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    terms_list = NaverAstro.objects.order_by('term')
    title = terms_list[0].source
    cnt = NaverAstro.objects.count()
    if kw:
        terms_list = terms_list.filter(
            Q(term__icontains=kw)  |
            Q(simple_sense__icontains=kw) |
            Q(eng__icontains=kw)
        ).distinct()
        cnt = terms_list.count()
    paginator = Paginator(terms_list, MAX_LIST_CNT)
    for page_num in paginator.page_range:
        last_page_num = last_page_num + 1
    last_page_num = last_page_num + 1
    page_obj = paginator.get_page(page)
    context = {'terms_list' : page_obj,
               'last_page_num' : last_page_num,
               'page' : page,
               'kw' : kw,
               'cnt' : cnt,
               'title' : title,
               }
    return render(request, 'southterms/terms_nastro_list.html', context)

def nBiochemiList(request):
    MAX_LIST_CNT = 10
    last_page_num = 0
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    terms_list = NaverBiochemi.objects.order_by('term')
    title = terms_list[0].source
    cnt = NaverBiochemi.objects.count()
    if kw:
        terms_list = terms_list.filter(
            Q(term__icontains=kw)  |
            Q(simple_sense__icontains=kw) |
            Q(eng__icontains=kw)
        ).distinct()
        cnt = terms_list.count()
    paginator = Paginator(terms_list, MAX_LIST_CNT)
    for page_num in paginator.page_range:
        last_page_num = last_page_num + 1
    last_page_num = last_page_num + 1
    page_obj = paginator.get_page(page)
    context = {'terms_list' : page_obj,
               'last_page_num' : last_page_num,
               'page' : page,
               'kw' : kw,
               'cnt' : cnt,
               'title' : title,
               }
    # print(last_page_num)
    return render(request, 'southterms/terms_nbiochemi_list.html', context)

def nBotanyList(request):
    MAX_LIST_CNT = 10
    last_page_num = 0
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    terms_list = NaverBotany.objects.order_by('term')
    title = terms_list[0].source
    cnt = NaverBotany.objects.count()
    if kw:
        terms_list = terms_list.filter(
            Q(term__icontains=kw)  |
            Q(simple_sense__icontains=kw) |
            Q(eng__icontains=kw)
        ).distinct()
        cnt = terms_list.count()
    paginator = Paginator(terms_list, MAX_LIST_CNT)
    for page_num in paginator.page_range:
        last_page_num = last_page_num + 1
    last_page_num = last_page_num + 1
    page_obj = paginator.get_page(page)
    context = {'terms_list' : page_obj,
               'last_page_num' : last_page_num,
               'page' : page,
               'kw' : kw,
               'cnt' : cnt,
               'title' : title,
               }
    # print(last_page_num)
    return render(request, 'southterms/terms_nbotany_list.html', context)

def nBuddhList(request):
    MAX_LIST_CNT = 10
    last_page_num = 0
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    terms_list = NaverBuddh.objects.order_by('term')
    title = terms_list[0].source
    cnt = NaverBuddh.objects.count()
    if kw:
        terms_list = terms_list.filter(
            Q(term__icontains=kw)  |
            Q(simple_sense__icontains=kw) |
            Q(eng__icontains=kw)
        ).distinct()
        cnt = terms_list.count()
    paginator = Paginator(terms_list, MAX_LIST_CNT)
    for page_num in paginator.page_range:
        last_page_num = last_page_num + 1
    last_page_num = last_page_num + 1
    page_obj = paginator.get_page(page)
    context = {'terms_list' : page_obj,
               'last_page_num' : last_page_num,
               'page' : page,
               'kw' : kw,
               'cnt' : cnt,
               'title' : title,
               }
    # print(last_page_num)
    return render(request, 'southterms/terms_nbuddh_list.html', context)

def nCellList(request):
    MAX_LIST_CNT = 10
    last_page_num = 0
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    terms_list = NaverCell.objects.order_by('term')
    title = terms_list[0].source
    cnt = NaverCell.objects.count()
    if kw:
        terms_list = terms_list.filter(
            Q(term__icontains=kw)  |
            Q(simple_sense__icontains=kw) |
            Q(eng__icontains=kw)
        ).distinct()
        cnt = terms_list.count()
    paginator = Paginator(terms_list, MAX_LIST_CNT)
    for page_num in paginator.page_range:
        last_page_num = last_page_num + 1
    last_page_num = last_page_num + 1
    page_obj = paginator.get_page(page)
    context = {'terms_list' : page_obj,
               'last_page_num' : last_page_num,
               'page' : page,
               'kw' : kw,
               'cnt' : cnt,
               'title' : title,
               }
    # print(last_page_num)
    return render(request, 'southterms/terms_ncell_list.html', context)

def nChemiList(request):
    MAX_LIST_CNT = 10
    last_page_num = 0
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    terms_list = NaverChemi.objects.order_by('term')
    title = terms_list[0].source
    cnt = NaverChemi.objects.count()
    if kw:
        terms_list = terms_list.filter(
            Q(term__icontains=kw)  |
            Q(simple_sense__icontains=kw) |
            Q(eng__icontains=kw)
        ).distinct()
        cnt = terms_list.count()
    paginator = Paginator(terms_list, MAX_LIST_CNT)
    for page_num in paginator.page_range:
        last_page_num = last_page_num + 1
    last_page_num = last_page_num + 1
    page_obj = paginator.get_page(page)
    context = {'terms_list' : page_obj,
               'last_page_num' : last_page_num,
               'page' : page,
               'kw' : kw,
               'cnt' : cnt,
               'title' : title,
               }
    # print(last_page_num)
    return render(request, 'southterms/terms_nchemi_list.html', context)

def nLifeList(request):
    MAX_LIST_CNT = 10
    last_page_num = 0
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    terms_list = NaverLife.objects.order_by('term')
    title = terms_list[0].source
    cnt = NaverLife.objects.count()
    if kw:
        terms_list = terms_list.filter(
            Q(term__icontains=kw)  |
            Q(simple_sense__icontains=kw) |
            Q(eng__icontains=kw)
        ).distinct()
        cnt = terms_list.count()
    paginator = Paginator(terms_list, MAX_LIST_CNT)
    for page_num in paginator.page_range:
        last_page_num = last_page_num + 1
    last_page_num = last_page_num + 1
    page_obj = paginator.get_page(page)
    context = {'terms_list' : page_obj,
               'last_page_num' : last_page_num,
               'page' : page,
               'kw' : kw,
               'cnt' : cnt,
               'title' : title,
               }
    # print(last_page_num)
    return render(request, 'southterms/terms_nlife_list.html', context)

def nChemiPediaList(request):
    MAX_LIST_CNT = 10
    last_page_num = 0
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    terms_list = NaverChemiPedia.objects.order_by('term')
    title = terms_list[0].source
    cnt = NaverChemiPedia.objects.count()
    if kw:
        terms_list = terms_list.filter(
            Q(term__icontains=kw)  |
            Q(simple_sense__icontains=kw) |
            Q(eng__icontains=kw)
        ).distinct()
        cnt = terms_list.count()
    paginator = Paginator(terms_list, MAX_LIST_CNT)
    for page_num in paginator.page_range:
        last_page_num = last_page_num + 1
    last_page_num = last_page_num + 1
    page_obj = paginator.get_page(page)
    context = {'terms_list' : page_obj,
               'last_page_num' : last_page_num,
               'page' : page,
               'kw' : kw,
               'cnt' : cnt,
               'title' : title,
               }
    # print(last_page_num)
    return render(request, 'southterms/terms_nchemipedia_list.html', context)
def nMathList(request):
    MAX_LIST_CNT = 10
    last_page_num = 0
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    terms_list = NaverMath.objects.order_by('term')
    title = terms_list[0].source
    cnt = NaverMath.objects.count()
    if kw:
        terms_list = terms_list.filter(
            Q(term__icontains=kw)  |
            Q(simple_sense__icontains=kw) |
            Q(eng__icontains=kw)
        ).distinct()
        cnt = terms_list.count()
    paginator = Paginator(terms_list, MAX_LIST_CNT)
    for page_num in paginator.page_range:
        last_page_num = last_page_num + 1
    last_page_num = last_page_num + 1
    page_obj = paginator.get_page(page)
    context = {'terms_list' : page_obj,
               'last_page_num' : last_page_num,
               'page' : page,
               'kw' : kw,
               'cnt' : cnt,
               'title' : title,
               }
    # print(last_page_num)
    return render(request, 'southterms/terms_nmath_list.html', context)

def nMeteoList(request):
    MAX_LIST_CNT = 10
    last_page_num = 0
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    terms_list = NaverMeteo.objects.order_by('term')
    title = terms_list[0].source
    cnt = NaverMeteo.objects.count()
    if kw:
        terms_list = terms_list.filter(
            Q(term__icontains=kw)  |
            Q(simple_sense__icontains=kw) |
            Q(eng__icontains=kw)
        ).distinct()
        cnt = terms_list.count()
    paginator = Paginator(terms_list, MAX_LIST_CNT)
    for page_num in paginator.page_range:
        last_page_num = last_page_num + 1
    last_page_num = last_page_num + 1
    page_obj = paginator.get_page(page)
    context = {'terms_list' : page_obj,
               'last_page_num' : last_page_num,
               'page' : page,
               'kw' : kw,
               'cnt' : cnt,
               'title' : title,
               }
    # print(last_page_num)
    return render(request, 'southterms/terms_nmeteo_list.html', context)

def nEarthList(request):
    MAX_LIST_CNT = 10
    last_page_num = 0
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    terms_list = NaverEarth.objects.order_by('term')
    title = terms_list[0].source
    cnt = NaverEarth.objects.count()
    if kw:
        terms_list = terms_list.filter(
            Q(term__icontains=kw)  |
            Q(simple_sense__icontains=kw) |
            Q(eng__icontains=kw)
        ).distinct()
        cnt = terms_list.count()
    paginator = Paginator(terms_list, MAX_LIST_CNT)
    for page_num in paginator.page_range:
        last_page_num = last_page_num + 1
    last_page_num = last_page_num + 1
    page_obj = paginator.get_page(page)
    context = {'terms_list' : page_obj,
               'last_page_num' : last_page_num,
               'page' : page,
               'kw' : kw,
               'cnt' : cnt,
               'title' : title,
               }
    # print(last_page_num)
    return render(request, 'southterms/terms_nearth_list.html', context)



def nGeoList(request):
    MAX_LIST_CNT = 10
    last_page_num = 0
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    terms_list = NaverGeo.objects.order_by('term')
    title = terms_list[0].source
    cnt = NaverGeo.objects.count()
    if kw:
        terms_list = terms_list.filter(
            Q(term__icontains=kw)  |
            Q(simple_sense__icontains=kw) |
            Q(eng__icontains=kw)
        ).distinct()
        cnt = terms_list.count()
    paginator = Paginator(terms_list, MAX_LIST_CNT)
    for page_num in paginator.page_range:
        last_page_num = last_page_num + 1
    last_page_num = last_page_num + 1
    page_obj = paginator.get_page(page)
    context = {'terms_list' : page_obj,
               'last_page_num' : last_page_num,
               'page' : page,
               'kw' : kw,
               'cnt' : cnt,
               'title' : title,
               }
    # print(last_page_num)
    return render(request, 'southterms/terms_ngeo_list.html', context)

def nOceanList(request):
    MAX_LIST_CNT = 10
    last_page_num = 0
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    terms_list = NaverOcean.objects.order_by('term')
    title = terms_list[0].source
    cnt = NaverOcean.objects.count()
    if kw:
        terms_list = terms_list.filter(
            Q(term__icontains=kw)  |
            Q(simple_sense__icontains=kw) |
            Q(eng__icontains=kw)
        ).distinct()
        cnt = terms_list.count()
    paginator = Paginator(terms_list, MAX_LIST_CNT)
    for page_num in paginator.page_range:
        last_page_num = last_page_num + 1
    last_page_num = last_page_num + 1
    page_obj = paginator.get_page(page)
    context = {'terms_list' : page_obj,
               'last_page_num' : last_page_num,
               'page' : page,
               'kw' : kw,
               'cnt' : cnt,
               'title' : title,
               }
    # print(last_page_num)
    return render(request, 'southterms/terms_nocean_list.html', context)






def nZooList(request):
    MAX_LIST_CNT = 10
    last_page_num = 0
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    terms_list = NaverZoo.objects.order_by('term')
    title = terms_list[0].source
    cnt = NaverZoo.objects.count()
    if kw:
        terms_list = terms_list.filter(
            Q(term__icontains=kw)  |
            Q(simple_sense__icontains=kw) |
            Q(eng__icontains=kw)
        ).distinct()
        cnt = terms_list.count()
    paginator = Paginator(terms_list, MAX_LIST_CNT)
    for page_num in paginator.page_range:
        last_page_num = last_page_num + 1
    last_page_num = last_page_num + 1
    page_obj = paginator.get_page(page)
    context = {'terms_list' : page_obj,
               'last_page_num' : last_page_num,
               'page' : page,
               'kw' : kw,
               'cnt' : cnt,
               'title' : title,
               }
    # print(last_page_num)
    return render(request, 'southterms/terms_nzoo_list.html', context)



def nMicroBioList(request):
    MAX_LIST_CNT = 10
    last_page_num = 0
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    terms_list = NaverMicroBio.objects.order_by('term')
    title = terms_list[0].source
    cnt = NaverMicroBio.objects.count()
    if kw:
        terms_list = terms_list.filter(
            Q(term__icontains=kw)  |
            Q(simple_sense__icontains=kw) |
            Q(eng__icontains=kw)
        ).distinct()
        cnt = terms_list.count()
    paginator = Paginator(terms_list, MAX_LIST_CNT)
    for page_num in paginator.page_range:
        last_page_num = last_page_num + 1
    last_page_num = last_page_num + 1
    page_obj = paginator.get_page(page)
    context = {'terms_list' : page_obj,
               'last_page_num' : last_page_num,
               'page' : page,
               'kw' : kw,
               'cnt' : cnt,
               'title' : title,
               }
    # print(last_page_num)
    return render(request, 'southterms/terms_nmicrobio_list.html', context)

def nFoodList(request):
    MAX_LIST_CNT = 10
    last_page_num = 0
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    terms_list = NaverFood.objects.order_by('term')
    title = terms_list[0].source
    cnt = NaverFood.objects.count()
    if kw:
        terms_list = terms_list.filter(
            Q(term__icontains=kw)  |
            Q(simple_sense__icontains=kw) |
            Q(eng__icontains=kw)
        ).distinct()
        cnt = terms_list.count()
    paginator = Paginator(terms_list, MAX_LIST_CNT)
    for page_num in paginator.page_range:
        last_page_num = last_page_num + 1
    last_page_num = last_page_num + 1
    page_obj = paginator.get_page(page)
    context = {'terms_list' : page_obj,
               'last_page_num' : last_page_num,
               'page' : page,
               'kw' : kw,
               'cnt' : cnt,
               'title' : title,
               }
    # print(last_page_num)
    return render(request, 'southterms/terms_nfood_list.html', context)



def nWaterList(request):
    MAX_LIST_CNT = 10
    last_page_num = 0
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    terms_list = NaverWater.objects.order_by('term')
    title = terms_list[0].source
    cnt = NaverWater.objects.count()
    if kw:
        terms_list = terms_list.filter(
            Q(term__icontains=kw)  |
            Q(simple_sense__icontains=kw) |
            Q(eng__icontains=kw)
        ).distinct()
        cnt = terms_list.count()
    paginator = Paginator(terms_list, MAX_LIST_CNT)
    for page_num in paginator.page_range:
        last_page_num = last_page_num + 1
    last_page_num = last_page_num + 1
    page_obj = paginator.get_page(page)
    context = {'terms_list' : page_obj,
               'last_page_num' : last_page_num,
               'page' : page,
               'kw' : kw,
               'cnt' : cnt,
               'title' : title,
               }
    # print(last_page_num)
    return render(request, 'southterms/terms_nwater_list.html', context)


def nMineList(request):
    MAX_LIST_CNT = 10
    last_page_num = 0
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    terms_list = NaverMine.objects.order_by('term')
    title = terms_list[0].source
    cnt = NaverMine.objects.count()
    if kw:
        terms_list = terms_list.filter(
            Q(term__icontains=kw)  |
            Q(simple_sense__icontains=kw) |
            Q(eng__icontains=kw)
        ).distinct()
        cnt = terms_list.count()
    paginator = Paginator(terms_list, MAX_LIST_CNT)
    for page_num in paginator.page_range:
        last_page_num = last_page_num + 1
    last_page_num = last_page_num + 1
    page_obj = paginator.get_page(page)
    context = {'terms_list' : page_obj,
               'last_page_num' : last_page_num,
               'page' : page,
               'kw' : kw,
               'cnt' : cnt,
               'title' : title,
               }
    # print(last_page_num)
    return render(request, 'southterms/terms_nmine_list.html', context)

def nWeatherList(request):
    MAX_LIST_CNT = 10
    last_page_num = 0
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    terms_list = NaverWeather.objects.order_by('term')
    title = terms_list[0].source
    cnt = NaverWeather.objects.count()
    if kw:
        terms_list = terms_list.filter(
            Q(term__icontains=kw)  |
            Q(simple_sense__icontains=kw) |
            Q(eng__icontains=kw)
        ).distinct()
        cnt = terms_list.count()
    paginator = Paginator(terms_list, MAX_LIST_CNT)
    for page_num in paginator.page_range:
        last_page_num = last_page_num + 1
    last_page_num = last_page_num + 1
    page_obj = paginator.get_page(page)
    context = {'terms_list' : page_obj,
               'last_page_num' : last_page_num,
               'page' : page,
               'kw' : kw,
               'cnt' : cnt,
               'title' : title,
               }
    # print(last_page_num)
    return render(request, 'southterms/terms_nweather_list.html', context)


def nGovernList(request):
    MAX_LIST_CNT = 10
    last_page_num = 0
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    terms_list = NaverGovern.objects.order_by('term')
    title = terms_list[0].source
    cnt = NaverGovern.objects.count()
    if kw:
        terms_list = terms_list.filter(
            Q(term__icontains=kw)  |
            Q(simple_sense__icontains=kw) |
            Q(eng__icontains=kw)
        ).distinct()
        cnt = terms_list.count()
    paginator = Paginator(terms_list, MAX_LIST_CNT)
    for page_num in paginator.page_range:
        last_page_num = last_page_num + 1
    last_page_num = last_page_num + 1
    page_obj = paginator.get_page(page)
    context = {'terms_list' : page_obj,
               'last_page_num' : last_page_num,
               'page' : page,
               'kw' : kw,
               'cnt' : cnt,
               'title' : title,
               }
    # print(last_page_num)
    return render(request, 'southterms/terms_ngovern_list.html', context)
