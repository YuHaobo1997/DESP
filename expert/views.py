from django.shortcuts import render

# Create your views here.
# from . import forms
from django.http import JsonResponse


def questionaire_submit(request):
    print(request.POST)
    return JsonResponse({'msg': 'success'})


def visualization(request):
    check_app = request.GET.get('app')
    return render(request, 'visual/overview_research.html', {'check_app': check_app})


