import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    # а я сделал с шаблоном =Р
    current_time = datetime.datetime.now().time().strftime('%H:%M')
    return render (request, 'app/current_time.html', context={'time': current_time})


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    directory = os.getcwd()
    files_list = os.listdir()
    return render(request, 'app/workdir.html', context={'files': files_list, 'dir': directory})
