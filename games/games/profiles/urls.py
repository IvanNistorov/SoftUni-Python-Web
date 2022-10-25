from django.urls import path, include

from games.profiles.views import *

urlpatterns = (
    path('', home_page, name='home page'),
    path('dashboard/', dashboard, name='dashboard'),

    path('profile/', include([
        path('create/', create_profile, name='create profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('details/', details_profile, name='details profile'),
        path('delete/', delete_profile, name='delete profile'),
    ])),
    path('game/', include([
        path('create/', created_game, name='create game'),
        path('edit/<int:pk>/', edit_game, name='edit game'),
        path('details/<int:pk>/', details_game, name='details game'),
        path('delete/<int:pk>/', delete_game, name='delete game'),
    ])))
