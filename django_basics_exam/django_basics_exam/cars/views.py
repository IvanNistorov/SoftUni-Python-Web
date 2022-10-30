from django.shortcuts import render, redirect

from django_basics_exam.cars.forms import CreateProfileForm, CreateCarForm, EditCarForm, DeleteCarForm, EditProfileForm
from django_basics_exam.cars.models import Profile, Car


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def index(request):
    profile = get_profile()

    context = {
        'profile': profile
    }

    return render(request, 'index.html', context)


def catalogue(request):
    car = Car.objects.all()

    context = {
        'cars': car,
    }

    return render(request, 'catalogue.html', context)


def create_profile(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'profile-create.html', context)


def details_profile(request):
    profile = get_profile()
    cars = Car.objects.all()

    if profile.first_name and profile.last_name:
        name_of_user = profile.fullname
    elif profile.first_name:
        name_of_user = profile.first_name
    elif profile.last_name:
        name_of_user = profile.last_name
    else:
        name_of_user = ''

    total_car_price = None
    if cars:
        total_car_price = sum(c.price for c in cars) / cars.count()

    context = {
        'profile': profile,
        'name_of_user': name_of_user,
        'total_car_price': total_car_price,
    }

    return render(request, 'profile-details.html', context)


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

    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    profile = get_profile()
    car = Car.objects.all()

    if request.method == 'POST':
        profile.delete()
        car.delete()
        return redirect('index')

    return render(request, 'profile-delete.html')


def create_car(request):
    if request.method == 'GET':
        form = CreateCarForm()
    else:
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'car-create.html', context)


def details_car(request, pk):
    car = Car.objects.filter(pk=pk).get()

    context = {
        'car': car,
    }

    return render(request, 'car-details.html', context)


def edit_car(request, pk):
    car = Car.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = EditCarForm(instance=car)
    else:
        form = EditCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'car': car,
    }

    return render(request, 'car-edit.html', context)


def delete_car(request, pk):
    car = Car.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = DeleteCarForm(instance=car)
    else:
        car.delete()
        return redirect('catalogue')

    context = {
        'form': form,
        'car': car,
    }

    return render(request, 'car-delete.html', context)
