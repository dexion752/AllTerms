from django.shortcuts import render
from django.http import HttpResponse

def indexTest(request):
    return HttpResponse("urls.py와 base_views.py 연동을 테스트 중입니다.")

# Create your views here.
