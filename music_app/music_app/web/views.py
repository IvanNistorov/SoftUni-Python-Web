from django.shortcuts import render, redirect

from music_app.web.forms import *
from music_app.web.models import Profile, Album


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def home_with_no_profile(request):
    profile = get_profile()

    if profile:
        return redirect('home page')

    if request.method == 'GET':
        form = AddProfileForm()
    else:
        form = AddProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
        'hide_navs': True,
    }

    return render(request, 'home-no-profile.html', context)


def home_with_profile(request):
    profile = get_profile()
    albums = Album.objects.all()

    if not profile:
        return redirect('add profile')

    context = {
        'profile': profile,
        'albums': albums
    }
    return render(request, 'home-with-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    album = Album.objects.all()

    if request.method == 'POST':
        profile.delete()
        album.delete()
        return redirect('home page')

    return render(request, 'profile-delete.html')


def details_profile(request):
    profile = get_profile()
    album = Album.objects.all()

    context = {
        'profile': profile,
        'album': album,
    }

    return render(request, 'profile-details.html', context)


def add_album(request):
    if request.method == 'GET':
        form = AddAlbumForm()
    else:
        form = AddAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
    }

    return render(request, 'add-album.html', context)


def details_album(request, pk):
    album = Album.objects.filter(pk=pk).get()

    context = {
        'album': album,
    }

    return render(request, 'album-details.html', context)


def delete_album(request, pk):
    album = Album.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = DeleteAlbumForm(instance=album)
    else:
        album.delete()
        return redirect('home page')

    context = {
        'form': form,
        'album': album,
    }

    return render(request, 'delete-album.html', context)


def edit_album(request, pk):
    album = Album.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = EditAlbumForm(instance=album)
    else:
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
        'album': album,
    }

    return render(request, 'edit-album.html', context)
