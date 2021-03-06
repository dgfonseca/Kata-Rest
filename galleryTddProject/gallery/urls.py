from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addUser/', views.add_user_view, name='addUser'),
    path('image/<int:params>', views.get_user_image, name='getUserImage'),
    path('login/', views.login_view, name='login'),
    path('putUser/<str:params>', views.put_user, name = 'putUser')
]
