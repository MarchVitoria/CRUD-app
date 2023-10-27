from django.contrib import admin
from django.urls import path
from schedule.views import *


urlpatterns = [
    path('', read),
    path('create/', create, name='create'),
    path('detail/<int:id>', detail, name='detail'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
]