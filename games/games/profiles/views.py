from django.shortcuts import render, redirect

from games.profiles.forms import CreateProfileForm, CreateGameForm, EditGameForm, DeleteGameForm, EditProfileForm
from games.profiles.models import Profile, Game


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def home_page(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    return render(request, 'home-page.html')


def dashboard(request):
    context = {
        'games': Game.objects.all(),
    }

    return render(request, 'dashboard.html', context)


def create_profile(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
    }

    return render(request, 'create-profile.html', context)


def details_profile(request):
    profile = get_profile()
    game = Game.objects.all()

    if profile.first_name and profile.last_name:
        name_of_user = profile.fullname
    elif profile.first_name:
        name_of_user = profile.first_name
    elif profile.last_name:
        name_of_user = profile.last_name
    else:
        name_of_user = ''

    try:
        game_rating = sum(r.rating for r in game) / len(game)
    except ZeroDivisionError:
        game_rating = float(0)

    context = {
        'profile': profile,
        'game': game,
        'game_rating': game_rating,
        'name_of_user': name_of_user,
    }

    return render(request, 'details-profile.html', context)


def edit_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'form': form,
    }

    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = Profile.objects.all()
    game = Game.objects.all()
    if request.method == 'POST':
        profile.delete()
        game.delete()
        return redirect('home page')

    return render(request, 'delete-profile.html')


def created_game(request):
    if request.method == 'GET':
        form = CreateGameForm()
    else:
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, 'create-game.html', context)


def details_game(request, pk):
    game = Game.objects.filter(pk=pk).get()

    context = {
        'game': game,
    }

    return render(request, 'details-game.html', context)


def edit_game(request, pk):
    game = Game.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = EditGameForm(instance=game)

    else:
        form = EditGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'game': game,
    }

    return render(request, 'edit-game.html', context)


def delete_game(request, pk):
    game = Game.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = DeleteGameForm(instance=game)

    else:
        game.delete()
        return redirect('dashboard')

    context = {
        'form': form,
        'game': game,
    }

    return render(request, 'delete-game.html', context)
