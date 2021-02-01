from django.shortcuts import render


def index(request):
    """Display the homepage."""

    return render(request, 'svhome/index.html', {})

def calendar(request):
    """Display the study calendar."""

    return render(request, 'svhome/calendar.html', {})