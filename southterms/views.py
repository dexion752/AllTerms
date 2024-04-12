from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from models import NaverAstro

from django.db.models import Q

# Create your views here.

def southIndex(request):
    MAX_LIST_CNT = 15
    last_page_num = 0
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    terms_list = NaverAstro.objects.order_by('-id')
    if kw:
        terms_list = terms_list.filter(
            Q(term=kw) # |
            # Q(content__icontains=kw) |
            # Q(answer__content__icontains=kw) |
            # Q(author__username__icontains=kw) |
            # Q(answer__author__username__icontains=kw)
        ).distinct()
    paginator = Paginator(terms_list, MAX_LIST_CNT)
    for page_num in paginator.page_range:
        last_page_num = last_page_num + 1
    page_obj = paginator.get_page(page)
    context = {'terms_list' : page_obj,
               'last_page_num' : last_page_num,
               'page' : page,
               'kw' : kw,
               }
    return render(request, 'southterms/terms_list.html', context)

