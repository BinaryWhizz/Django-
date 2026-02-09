
from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.all_binary, name='all_binary'),
    # path('order/', views.order, name='order')
    path('<int:binary_id>/', views.binary_descp, name='binary_description'),
    path('binaryStudent/', views.binary_student, name='binary_student'),

]

