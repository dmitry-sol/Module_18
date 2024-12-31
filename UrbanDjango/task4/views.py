from django.shortcuts import render

def index(request):
    return render(request, 'fourth_task/index.html')

def page1(request):
    items = {'items': ['Витамины', 'Добавки', 'Литература']}
    return render(request,
             'fourth_task/page1.html',
            {'items': items})

def page2(request):
    return render(request,
              'fourth_task/page2.html')
