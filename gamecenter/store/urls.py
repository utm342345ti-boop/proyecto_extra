from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [
path("", views.home,name="home"),
path("catalog/", views.catalog, name="catalog"),
path("product/<int:id>/",views.product_detail, name="product_detail"),

]

urlpatterns = [
    path('', views.index, name='index'),
    path('catalogo/', views.catalog, name='catalog'),
    path('producto/<slug:slug>/', views.product_detail, name='product_detail'),
    path('proveedores/contacto/', views.contact_provider, name='contact_provider'),
]

