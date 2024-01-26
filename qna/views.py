from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

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


@login_required(login_url='common:login')
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('qna:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question' : question, 'form' : form}
    return render(request, 'qna/question_detail.html', context)


@login_required(login_url='common:login')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.create_date = timezone.now()
            question.save()
            return redirect('qna:index')
    else:
        form = QuestionForm()
    context = {'form' : form}
    # {'form' : form} 은 템플릿에서 질문 등록 시 사용할 폼 엘리먼트를 생성할 때 사용
    return render(request, 'qna/question_form.html', context)

# Create your views here.
