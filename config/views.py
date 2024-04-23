from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexTest(request):
    return HttpResponse("urls.py와 base_views.py 연동을 테스트 중입니다.")

# def index(request):
#     return HttpResponse("<h1><p style='text-align:center;'>겨레말큰사전남북공동편찬사업회<br>남북 전문용어 허브</p></h1>")


def index(request):
    # context = { msg : "<h1><p style='text-align:center;'>겨레말큰사전남북공동편찬사업회<br>남북 전문용어 허브</p></h1>" }

    return render(request, 'common/index.html')