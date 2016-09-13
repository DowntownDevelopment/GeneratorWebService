from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.db.models import Count
from django.shortcuts import render, render_to_response
from django.utils import timezone
from .models import RandomPage
from .generate import main


def html_list(request):
    print('Building List...')
    html = RandomPage.objects.filter(date_generated__lte=timezone.now()).order_by('date_generated')
    return render(request, 'webgen/html_list.html', {'html': html})


def generate(request):
    print('Generating Page...')
    html_page = main.build_web_page()
    return render(request, 'webgen/generated_site.html', {'html_page': html_page})


def dashboard(request):
    print('Setting up Dashboard...')
    html = RandomPage.objects.filter(date_generated__lte=timezone.now()).order_by('date_generated')
    return render(request, 'webgen/dashboard.html', {'html': html})


def gener8(request):
    print('Generating Page...')
    title = main.username()
    content = main.content()
    # css = main.css()
    # js = main.js()
    return render(request, 'webgen/gener8.html', {'title': title, 'content': content})
