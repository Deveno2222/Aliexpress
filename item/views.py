from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import NewProductForm, EditProductForm
from reviews.forms import ReviewForm

# Create your views here.
def detail(request, pk):
  product = get_object_or_404(Product, pk=pk)
  related_products = Product.objects.filter(category=product.category, is_sold=False).exclude(pk=pk)[0:3]

  
  if request.method == 'POST' and request.user.is_authenticated:
    form = ReviewForm(request.POST)
    if form.is_valid():
      review = form.save(commit=False)
      review.user = request.user
      review.product = product
      review.save()
      return redirect('item:detail', pk=pk)
  else:
    form = ReviewForm()



  return render(request, 'item/detail.html', {
    'product': product,
    'related_products': related_products,
    'form': form,
  })


@login_required
def create(request):
  if request.method == 'POST':
    form = NewProductForm(request.POST, request.FILES)

    if form.is_valid():
      product = form.save(commit=False)
      product.created_by = request.user
      product.save()

      return redirect('item:detail', pk=product.id)
  else:
    form = NewProductForm()

  return render(request, 'item/create.html',{
    'form': form,
    'title': 'Create Product',
  })

@login_required
def edit(request, pk):
  product = get_object_or_404(Product, pk=pk, created_by=request.user)
  if request.method == 'POST':
    form = EditProductForm(request.POST, request.FILES, instance=product)

    if form.is_valid():
      form.save()

      return redirect('item:detail', pk=product.id)
  else:
    form = EditProductForm(instance=product)

  return render(request, 'item/create.html',{
    'form': form,
    'title': 'Edit Product',
  })

@login_required
def delete(request, pk):
  product = get_object_or_404(Product, pk=pk, created_by=request.user)
  product.delete()

  return redirect('dashboard:index')
