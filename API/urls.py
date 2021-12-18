from django.urls import path
from .views import listProd, listProdDetail, export

urlpatterns = [
    path('', listProd.as_view()),
    path('<int:pk>', listProdDetail.as_view()),
    path('export/', export),
]