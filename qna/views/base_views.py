from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question

def index(request):
    MAX_LIST_CNT = 15
    last_page_num = 0
    page = request.GET.get('page', '1')
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list, MAX_LIST_CNT)
    for page_num in paginator.page_range:
        last_page_num = last_page_num + 1
    page_obj = paginator.get_page(page)
    context = {'question_list' : page_obj,
               'last_page_num' : last_page_num,
               }
    return render(request, 'qna/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = { 'question' : question }
    return render(request, 'qna/question_detail.html', context)
