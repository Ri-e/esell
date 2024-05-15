from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('product/<str:pk>', views.product, name='product'),
    path('create/', views.create, name ='create'),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('delete/<str:pk>', views.delete, name='delete'),
    path('update/<str:pk>', views.update, name='update')

]
