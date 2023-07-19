from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect

from item.models import Category, Product

from .forms import SignUpForm
# Create your views here.

def index(request):
  products = Product.objects.filter(is_sold=False)
  categories = Category.objects.all()

  return render(request, "core/index.html", {
    'categories': categories,
    'products': products,
  })
  
def signup(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)

    if form.is_valid():
      form.save()

      return redirect('/login/')
  else:
    form = SignUpForm()

  return render(request, 'core/signup.html', {
    'form': form
  })

def logout_view(request):
    logout(request)
    return redirect('/')