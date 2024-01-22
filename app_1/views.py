#from django.shortcuts import render

# Create your views here.

import logging
from django.http import HttpResponse, HttpRequest


def index(request: HttpRequest):
    html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Задание 8</title>
</head>
<body>
    <h1>Это главная страница сайта на Django.</h1>
    <h3>Она находится по адресу: {request.get_host() + request.path}</h3>
</body>
</html>
    """
    logger.debug('Index page requested.')
    
    return HttpResponse(html)

def about(request: HttpRequest):
    html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Задание 8</title>
</head>
<body>
    <h1>Это страница обо мне.</h1>
    <h3>Она находится по адресу: {request.get_host()  + request.path}</h3>
</body>
</html>
    """
    logger.debug('About page requested.')

    return HttpResponse(html)

logger = logging.getLogger(__name__)