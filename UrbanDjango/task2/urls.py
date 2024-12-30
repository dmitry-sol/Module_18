from django.urls import path
from .views import index, func_template, ClassTemplate


urlpatterns = [
    path('', index, name='second_index'),
    path('class_template', func_template, name='funk_template'),
    path('func_template', ClassTemplate.as_view(), name='class_template'),
]