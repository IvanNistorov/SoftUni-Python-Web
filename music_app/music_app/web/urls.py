from django.urls import path, include

from music_app.web.views import *

urlpatterns = (
    path('', home_with_profile, name='home page'),
    path('album/', include([
        path('add/', add_album, name='add album'),
        path('details/<int:pk>/', edit_album, name='edit album'),
        path('edit/<int:pk>/', details_album, name='details album'),
        path('delete/<int:pk>/', delete_album, name='delete album'),
    ])),
    path('profile/details/', details_profile, name='details profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
    path('profile/add/', home_with_no_profile, name='add profile'),

)
