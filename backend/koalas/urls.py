from django.urls import path

from . import views
# /api/products/
urlpatterns = [
    path('', views.koala_list_view),
    path('', views.koala_create_view),
    path('<int:pk>/', views.koala_detail_view)
]