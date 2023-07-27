from django.shortcuts import render, redirect
from .forms import CategoryForm
from item.models import Category

# Create your views here.

def category_list(request):
  categories = Category.objects.all()
  return render(request,'category/category_list.html', {
    'categories': categories,
  })

def add_category(request):
  if request.user.is_superuser:
    if request.method == 'POST':
      form = CategoryForm(request.POST)
      if form.is_valid():
        category_name = form.cleaned_data['name']
        if Category.objects.filter(name=category_name).exists():
          form.add_error('name', 'This category already exists.')
        else:
          form.save()
          return redirect('category:category_list')
    else:
      form = CategoryForm()
    return render(request, 'category/add_category.html', {'form': form})
  else:
    return redirect('category:error')

def error(request):
  return render(request, 'category/error.html')




