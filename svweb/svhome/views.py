from django.shortcuts import render


def index(request):
    """Display the homepage."""

    return render(request, 'svhome/index.html', {})