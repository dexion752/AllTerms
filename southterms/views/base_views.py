from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from ..models import *

from django.db.models import Q

# Create your views here.

def indexTest(request):
    return HttpResponse("urls.py와 base_views.py 연동을 테스트 중입니다.")

def srcList(request):
    MAX_LIST_CNT = 10
    last_page_num = 0
    last_page_num_n = 0
    last_page_num_s = 0
    total_s = 0
    total_n = 0
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    terms_list = Sources.objects.order_by('title')
    terms_list_s = Sources.objects.filter(code='s').order_by('title')
    terms_list_n = Sources.objects.filter(code='n').order_by('title')
    print(terms_list_s)
    print(terms_list_n)
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
    paginator_n = Paginator(terms_list_n, MAX_LIST_CNT)
    paginator_s = Paginator(terms_list_s, MAX_LIST_CNT)

    for page_num in paginator.page_range:
        last_page_num = last_page_num + 1
    last_page_num = last_page_num + 1

    for page_num in paginator_n.page_range:
        last_page_num_n = last_page_num_n + 1
    last_page_num_n = last_page_num_n + 1

    for page_num in paginator_s.page_range:
        last_page_num_s = last_page_num_s + 1
    last_page_num_s = last_page_num_s + 1

    page_obj = paginator.get_page(page)
    page_obj_n = paginator_n.get_page(page)
    page_obj_s = paginator_s.get_page(page)
    context = {'terms_list' : page_obj,
               'terms_list_n' : page_obj_n,
               'terms_list_s' : page_obj_s,
               'last_page_num' : last_page_num,
               'last_page_num_n' : last_page_num_n,
               'last_page_num_s' : last_page_num_s,
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


def nEcohkList(request):
    MAX_LIST_CNT = 10
    last_page_num = 0
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    terms_list = NaverEcoHK.objects.order_by('term')
    title = terms_list[0].source
    cnt = NaverEcoHK.objects.count()
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
    return render(request, 'southterms/terms_necohk_list.html', context)

def nLiterList(request):
    MAX_LIST_CNT = 10
    last_page_num = 0
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    terms_list = NaverLiter.objects.order_by('term')
    title = terms_list[0].source
    cnt = NaverLiter.objects.count()
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
    return render(request, 'southterms/terms_nliter_list.html', context)

def nChurchList(request):
    MAX_LIST_CNT = 10
    last_page_num = 0
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    terms_list = NaverChurch.objects.order_by('id')
    title = terms_list[0].source
    cnt = NaverChurch.objects.count()
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
    return render(request, 'southterms/terms_nchurch_list.html', context)

def nObuddhList(request):
    MAX_LIST_CNT = 10
    last_page_num = 0
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    terms_list = NaverObuddh.objects.order_by('term')
    title = terms_list[0].source
    cnt = NaverObuddh.objects.count()
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
    return render(request, 'southterms/terms_nobuddh_list.html', context)

def nReligionList(request):
    MAX_LIST_CNT = 10
    last_page_num = 0
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    terms_list = NaverReligion.objects.order_by('term')
    title = terms_list[0].source
    cnt = NaverReligion.objects.count()
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
    return render(request, 'southterms/terms_nreligion_list.html', context)

def nSajuList(request):
    MAX_LIST_CNT = 10
    last_page_num = 0
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    terms_list = NaverSaju.objects.order_by('term')
    title = terms_list[0].source
    cnt = NaverSaju.objects.count()
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
    return render(request, 'southterms/terms_nsaju_list.html', context)


def nMediSeoulList(request):
    MAX_LIST_CNT = 10
    last_page_num = 0
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    terms_list = NaverMediSeoul.objects.order_by('term')
    title = terms_list[0].source
    cnt = NaverMediSeoul.objects.count()
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
    return render(request, 'southterms/terms_nmediseoul_list.html', context)


def nMediRareList(request):
    MAX_LIST_CNT = 10
    last_page_num = 0
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    terms_list = NaverMedirare.objects.order_by('term')
    title = terms_list[0].source
    cnt = NaverMedirare.objects.count()
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
    return render(request, 'southterms/terms_nmedirare_list.html', context)


def nNurseList(request):
    MAX_LIST_CNT = 10
    last_page_num = 0
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    terms_list = NaverNurse.objects.order_by('term')
    title = terms_list[1].source
    cnt = NaverNurse.objects.count()
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
    return render(request, 'southterms/terms_nnurse_list.html', context)

def nDrugList(request):
    MAX_LIST_CNT = 10
    last_page_num = 0
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    terms_list = NaverDrug.objects.order_by('term')
    title = terms_list[1].source
    cnt = NaverDrug.objects.count()
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
    return render(request, 'southterms/terms_ndrug_list.html', context)

def nMediShortList(request):
    MAX_LIST_CNT = 10
    last_page_num = 0
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    terms_list = NaverMediShort.objects.order_by('id')
    title = terms_list[1].source
    cnt = NaverMediShort.objects.count()
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
    return render(request, 'southterms/terms_nmedishort_list.html', context)

def nMediBodyList(request):
    MAX_LIST_CNT = 10
    last_page_num = 0
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    terms_list = NaverMediBody.objects.order_by('term')
    title = terms_list[1].source
    cnt = NaverMediBody.objects.count()
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
    return render(request, 'southterms/terms_nmedibody_list.html', context)

def nDiseaseList(request):
    MAX_LIST_CNT = 10
    last_page_num = 0
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    terms_list = NaverDisease.objects.order_by('term')
    title = terms_list[1].source
    cnt = NaverDisease.objects.count()
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
    return render(request, 'southterms/terms_ndisease_list.html', context)

def nPharmacyList(request):
    MAX_LIST_CNT = 10
    last_page_num = 0
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    terms_list = NaverPharmacy.objects.order_by('term')
    title = terms_list[1].source
    cnt = NaverPharmacy.objects.count()
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
    return render(request, 'southterms/terms_npharmacy_list.html', context)

