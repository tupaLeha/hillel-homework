import string
import random

from django.http import HttpResponse
from django.shortcuts import render
from string import ascii_letters, punctuation, digits
from random import choices


def get_random_str(length, specials, numbers):
    error = None
    try:
        length = int(length)
    except ValueError:
        return None, 'Length should be int'

    if numbers not in (None, '1'):
        return None, 'Numbers should be 0 or 1'

    if specials not in (None, '1'):
        return None, 'Specials should be 0 or 1'

    if length < 1 or length > 100:
        return None, 'Length should be in [1, 100]'
    chars = string.ascii_letters

    if specials:
        chars += string.punctuation
    if numbers:
        chars += string.digits

    res = ''
    if length and not error:
        res = ''.join(random.choices(chars, k=length))

    return res, error


def index(request):
    length = request.GET['length']
    specials = request.GET['specials']
    numbers = request.GET['digits']

    res, error = get_random_str(length, specials, numbers)

    return HttpResponse(res, error)

