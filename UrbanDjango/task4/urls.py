from django.urls import path
from .views import index, page1, page2  # Импортируем представления

urlpatterns = [
    path('', index, name='fourth_index'), # Главная страница
    path('page1', page1, name='fourth_page1'),  # Первая страница
    path('page2', page2, name='fourth_page2'),  # Вторая страница
]