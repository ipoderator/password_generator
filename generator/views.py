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
    characters = list('abcdefghijklmnopqrstwxyz') # Список для генерации простых паролей

    if request.GET.get('uppercase'):
        """ Добавление нужного нам списка """
        characters.extend(list('ABCDEFGHIGKLMNOPQRSTWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    """
     Функция для генерации длинны пароля из запроса пользователя, 
    с заданной длинной в 12 символов и значение length == length
    из html файла <select name="length"> 
    """
    length = int(request.GET.get('length', 12)) # Длина пароля

    thepassword = ''
    """ Функция для добавляние буквы в нижнем регистре"""
    for x in range(length):
        thepassword += random.choice(characters) # Choice выбирает случайные буквы
    
    return render(request, 'generator/password.html', {'password':thepassword})

