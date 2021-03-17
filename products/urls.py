from django.urls import path

from products.views import product_list_view, product_create_view, product_detail_view, product_delete_view

app_name = 'products'
urlpatterns = [
    path('', product_list_view, name='product-list'),
    path('create/', product_create_view, name='product-create'),
    path('<int:current_id>/', product_detail_view, name='product-detail'),
    path('<int:current_id>/delete/', product_delete_view, name='product-delete'),
]
