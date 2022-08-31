from django.shortcuts import render, HttpResponse, redirect
from .models import Category, Dish, Event, Gallery, Chefs, WhyUs, AboutUs, Testimonials
from .forms import UserReservationForm


def base(request):
    if request.method == 'POST':
        reservation = UserReservationForm(request.POST)
        if reservation.is_valid():
            reservation.save()
            return redirect('/')

    categories = Category.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True)
    special = Dish.objects.filter(special=True)
    event = Event.objects.filter(is_visible=True)
    gallery = Gallery.objects.filter(is_visible=True)
    chefs = Chefs.objects.filter(is_visible=True)
    why_us = WhyUs.objects.filter(is_visible=True)
    about = AboutUs.objects.filter()[0]
    testimonials = Testimonials.objects.filter(is_visible=True)
    reservation = UserReservationForm()

    data = {'categories': categories,
            'dishes': dishes,
            'specials': special,
            'events': event,
            'gallery': gallery,
            'chefs': chefs,
            'why_us': why_us,
            'about': about,
            'testimonials': testimonials,
            'reservation_form': reservation
            }

    return render(request, 'base.html', context=data)
