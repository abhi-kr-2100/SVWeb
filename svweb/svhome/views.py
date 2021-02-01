from django.http.response import HttpResponse
from django.shortcuts import render


def index(request):
    """Display the homepage."""

    return render(request, 'svhome/index.html', {})


def calendar(request):
    """Display the study calendar."""

    return render(request, 'svhome/calendar.html', {
        'tz': 'Europe/Brussels',
        'err': None
    })


def calendar_tz(request, country):
    """Display the study calendar in the given country's timezone."""

    tz = get_timezone(country)
    if tz is not None:
        return render(request, 'svhome/calendar.html', {
            'tz': tz,
            'err': None
        })
    else:
        return render(request, 'svhome/calendar.html', {
            'tz': 'Europe/Brussels',
            'err': f'{country}'
        })


def study_tips(request):
    """Display a list of saved study tips."""

    return render(request, 'svhome/study_tips.html', {})


def social_media(request):
    """Display a list of social media on which Study Vibes is active."""

    return render(request, 'svhome/social_media.html', {})


def about(request):
    "About Study Vibes."

    return render(request, 'svhome/about.html', {})


def get_timezone(country):
    """Return the timezone for the given country."""

    timezones = {
        'america':  'US/Eastern',
        'us':       'US/Eastern',
        'belgium':  'Europe/Brussels',
        'turkey':   'Europe/Istanbul',
        'india':    'Asia/Kolkata'
    }

    return timezones.get(country.lower())