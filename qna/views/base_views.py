from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question

from django.db.models import Q

def qnaIndex(request):
    MAX_LIST_CNT = 15
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    question_list = Question.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |
            Q(content__icontains=kw) |
            # Q(answer__content__icontains=kw) |
            # Q(answer__author__username__icontains=kw) |
            Q(author__username__icontains=kw)
        ).distinct()
    paginator = Paginator(question_list, MAX_LIST_CNT)
    page_obj = paginator.get_page(page)
    context = {'question_list' : page_obj,
               'page' : page,
               'kw' : kw,
               }
    return render(request, 'qna/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = { 'question' : question }
    return render(request, 'qna/question_detail.html', context)
