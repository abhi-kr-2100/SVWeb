from django.http.response import HttpResponse
from django.shortcuts import render


def index(request):
    """Display the homepage."""

    return render(request, 'svhome/index.html', {})


def calendar(request):
    """Display the study calendar."""

    return render(request, 'svhome/calendar.html', {})


def study_tips(request):
    """Display a list of saved study tips."""

    return HttpResponse("Not implemented yet.")


def social_media(request):
    """Display a list of social media on which Study Vibes is active."""

    return HttpResponse("Not implemented yet.")


def about(request):
    "About Study Vibes."

    return HttpResponse("Not implemented yet.")