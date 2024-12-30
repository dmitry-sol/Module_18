from django.shortcuts import render

def index(request):
    return render(request, 'third_task/index.html')

def page1(request):
    items = {
        'item1': 'Витамины',
        'item2': 'Добавки',
        'item3': 'Литература',
    }
    return render(request, 'third_task/page1.html', {'items': items})

def page2(request):
    return render(request, 'third_task/page2.html')
