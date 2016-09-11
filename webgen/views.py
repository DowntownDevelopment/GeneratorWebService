from django.shortcuts import render, render_to_response
from django.utils import timezone
from .models import RandomPage


def html_list(request):
    html = RandomPage.objects.filter(date_generated__lte=timezone.now()).order_by('date_generated')
    return render(request, 'webgen/html_list.html', {'html': html})
