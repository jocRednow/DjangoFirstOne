from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .models import Product
from .form import ProductForm, RowProductForm


def product_create_view(request):
    my_form = RowProductForm()
    if request.method == 'POST':
        my_form = RowProductForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        'form': my_form
    }
    return render(request, "products/product_create.html", context)

# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#     context = {
#         'form': form
#     }
#     return render(request, "products/product_create.html", context)


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'products/product_list.html', context)


def product_detail_view(request, current_id):
    obj = get_object_or_404(Product, id=current_id)
    obj = Product.objects.get(id=current_id)
    try:
        obj = Product.objects.get(id=current_id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)


def product_delete_view(request, current_id):
    obj = get_object_or_404(Product, id=current_id)
    if request.method == 'POST':
        obj.delete()
        return redirect('../../')
    context = {
        'object': obj
    }
    return render(request, 'products/product_delete.html', context)
