from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from ..models import NaverAstro

from django.db.models import Q

# Create your views here.

def indexTest(request):
    return HttpResponse("urls.py와 base_views.py 연동을 테스트 중입니다.")

def southSources(request):
    src = SouthSrc.objects.all()
    context = { 'src' : src,
                }
    return render(request, 'common/southsrc.html', context)

def astroList(request):
    MAX_LIST_CNT = 10
    last_page_num = 0
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    terms_list = NaverAstro.objects.order_by('term')
    cnt = NaverAstro.objects.count()
    if kw:
        terms_list = terms_list.filter(
            Q(term__icontains=kw)  |
            Q(simple_sense__icontains=kw) |
            Q(eng__icontains=kw)
        ).distinct()
    paginator = Paginator(terms_list, MAX_LIST_CNT)
    # for page_num in paginator.page_range:
    #     last_page_num = last_page_num + 1
    last_page_num = last_page_num + 1
    page_obj = paginator.get_page(page)
    context = {'terms_list' : page_obj,
               'last_page_num' : last_page_num,
               'page' : page,
               'kw' : kw,
               'cnt' : cnt,
               }
    return render(request, 'southterms/terms_list.html', context)

