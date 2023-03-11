from django.shortcuts import render
import random

# Main page
def home(request):
    return render(request, 'generator/home.html')

# Page with the password
def password(request):
# Array of the letters
    characters = list('abcdefghijklmnopqrstuvwxyz')
# Consider the terms of the request
    # Capital letters
    if request.GET.get('uppercheck'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    # Numbers
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    # Special characters
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()-_=+'))
# Length of the password
    length = int(request.GET.get('length',12))
    thepassword = ''
# Generating of the password
    for x in range(length):
        thepassword += random.choice(characters)
# This is about page and list wich we provide to the page
    return render(request, 'generator/password.html', {'password': thepassword})

