from django.shortcuts import render
import random


""" Функция вызова домашней страницы """
def home(request):
    return render(request, 'generator/home.html') # Вызов html файла на домашней странице


""" Описание проекта """
def description(request):
    return render(request, 'generator/description.html')


""" Основной код проекта """
def password(request):
    characters = list('abcdefghijklmnopqrstwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIGKLMNOPQRSTWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    length = int(request.GET.get('length', 12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
    
    return render(request, 'generator/password.html', {'password':thepassword})



    