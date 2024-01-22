from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("안녕하세요. <br>질문과 답변 게시판에 오신 것을 환영합니다.")

# Create your views here.
