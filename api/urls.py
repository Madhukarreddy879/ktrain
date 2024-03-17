from django.urls import path
from .views import health, ItemList, ItemDetail, LocationDetail, LocationList

urlpatterns = [
    path('health/', health),
    path('location/', LocationList.as_view()),
    path('location/<int:pk>/', LocationDetail.as_view()),
    path('item/', ItemList.as_view()),
    path('item/<int:pk>/', ItemDetail.as_view()),
]
