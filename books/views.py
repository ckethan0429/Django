from django.shortcuts import render
from datetime import datetime
import random
import requests
import os

# Create your views here.
def index(request):
    return render(request, 'books/index.html')


def graduation(request):
    end = datetime(2019, 6, 27)
    now = datetime.now()
    gap = end - now
    print(end)
    print(now)

    context = {
        'now': now,
        'end': end,
        'gap': gap,
    }
    return render(request, 'books/graduation.html', context)


def imagepick(request):
    random_pick = random.randrange(1,1000)
    print(random_pick)
    url = f'https://picsum.photos/id/{random_pick}/500/500'
    context = {
        'random_pick': random_pick,
        'url': url,
    }

    return render(request, 'books/imagepick.html', context)


def today(request):

    url = "https://api.openweathermap.org/data/2.5/weather?q=Seoul,kr&lang=kr&APPID=9703800a5ed775ca5caaabf39362a3ad"
    today_weather = requests.get(url).json()

    status = today_weather['weather'][0]['description']

    temp = list(today_weather['main'].values())
    print(type(temp[0]))
    temp_now = round(-273.15+temp[0],1)
    temp_min = -273.15+temp[3]
    temp_max = -273.15+temp[4]
    context= {
        'status': status,
        'temp_now': temp_now,
        'temp_min': temp_min,
        'temp_max': temp_max,
    }
    print(context)

    return render(request, 'books/today.html', context)


def ascii_new(request):
    fonts = ['short', 'utopia', 'rounded', 'acrobatic', 'alligator']
    context = {'fonts': fonts,}
    return render(request, 'books/ascii_new.html', context)


def ascii_make(request):
    text = request.GET.get('text')
    font = request.GET.get('font')
    url = f'http://artii.herokuapp.com/make?text={text}&font={font}'
    result = requests.get(url).text
    context = {'result': result,}
    return render(request, 'books/ascii_make.html', context)


def original(request):
    return render(request, 'books/original.html')


def translated(request):
    korean = request.GET.get('text')
    naver_client_id = os.getenv("NAVER_CLIENT_ID")
    naver_client_secret = os.getenv("NAVER_CLIENT_SECRET")

    papago_url = "https://openapi.naver.com/v1/papago/n2mt"

    # 네이버에 Post 요청을 위해서 필요한 내용들
    headers = {
        "X-Naver-Client-Id": naver_client_id,
        "X-Naver-Client-Secret": naver_client_secret
    }

    data = {
        "source": "ko",
        "target": "en",
        "text": korean
    }

    papago_response = requests.post(papago_url, headers=headers, data=data).json()
    english = papago_response["message"]["result"]["translatedText"]

    context = {
        'korean': korean,
        'english': english,

    }
    return render(request, 'books/translated.html', context)

