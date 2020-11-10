from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from covid19.models import covid19


def home(request):
    covid19_data = covid19.objects.all()
    context = {
        "covid19": covid19_data,
    }
    return render(request, 'pages/index.html', context)
