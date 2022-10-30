from django.urls import path, include

from django_basics_exam.cars.views import *

urlpatterns = (
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalogue'),
    path('profile/', include([
        path('create/', create_profile, name='create profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('details/', details_profile, name='details profile'),
        path('delete/', delete_profile, name='delete profile'),
    ])),
    path('car/', include([
        path('create/', create_car, name='create car'),
        path('<int:pk>/edit/', edit_car, name='edit car'),
        path('<int:pk>/details/', details_car, name='details car'),
        path('<int:pk>/delete/', delete_car, name='delete car'),
    ])))