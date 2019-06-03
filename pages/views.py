from django.shortcuts import render
import random
import math
#from pprint import pprint
# Create your views here.


def index(request):

    return render(request, 'index.html')


def dinner(request):

    menus = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menus)
    context = {'pick': pick}
    return render(request, 'dinner.html', context)


def hello(request, name):

    context = {'name': name,}
    return render(request, 'hello.html',context)

# 자기소개/ 이름과 나이를 url로 받아서 출력
def introduce(request, name, age):
    context = {'name': name,
              'age': age,
               }
    return render(request, 'introduce.html', context)

# 숫자 2개를 variable routing으로 받아 곱셈결과를 출력


def times(request, num_1, num_2):
    value = num_1 * num_2
    context={'num_1': num_1,
             'num_2': num_2,
             'value': value,
            }
    return render(request, 'times.html', context)

# 원의 반지름 값을 variable routing 으로 받아 원의 넓이를 출력
def area(request, radius):
    value = math.pi * radius * radius
    context = {'radius': radius,
               'value': value,
               }
    return render(request, 'area.html', context)
