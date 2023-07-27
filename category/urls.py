from django.urls import path
from . import views

app_name = 'category'

urlpatterns = [
  path('category_list/', views.category_list, name='category_list'),
  path('add_category/',views.add_category, name='add_category'),
  path('error/',views.error, name='error'),
]