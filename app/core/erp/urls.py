from django.urls import path
from core.erp.views.category.views import *

app_name = 'erp'

urlpatterns = [
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('category/API/', ListCategory.as_view(),name='apiRest'),
    path('category/API/<int:pk>', ListCategoryDetail.as_view(),name='category_Detail'),
    path('category/API/delete/<int:pk>', DeleteCategory.as_view(),name='category_Delete'),

    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('product/API/', ListProduct.as_view(),name='apiProducto'),
    path('product/API/<int:pk>', ListProductDetail.as_view(),name='product_Detail'),
    path('product/API/delete/<int:pk>', DeleteProduct.as_view(),name='product_Delete'),

]
