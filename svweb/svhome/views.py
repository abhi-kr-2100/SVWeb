from django.conf import settings
from django.shortcuts import render


from .models import StudyTip


def index(request):
    """Display the homepage."""

    return render(request, 'svhome/index.html', {})

def calendar(request, country="Belgium"):
    """Display the study calendar in the given country's timezone."""

    tz = get_timezone(country)
    countries = get_countries()
    err = None

    if tz is None:
        tz = get_timezone('Belgium')
        err = country

    return render(request, 'svhome/calendar.html', {
        'tz': tz,
        'err': err,
        'timezones': countries
    })

def study_tips(request):
    """Display a list of saved study tips."""

    tips = StudyTip.objects.all()
    if tips:
        ctx = {'tips': tips}
    else:
        ctx = {}

    return render(request, 'svhome/study_tips.html', ctx)


def social_media(request):
    """Display a list of social media on which Study Vibes is active."""

    return render(request, 'svhome/social_media.html', {})


def about(request):
    "About Study Vibes."

    return render(request, 'svhome/about.html', {})


def get_timezone(country):
    """Return the timezone for the given country."""

    return settings.TIMEZONES.get(country.replace(" ", "-"))

def get_countries():
    """Return all countries for which TZ data is available."""

    return [c.replace("-", " ") for c in settings.TIMEZONES.keys()]