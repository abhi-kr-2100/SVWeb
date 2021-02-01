from django.shortcuts import render


def index(request):
    """Display the homepage."""

    render(request, 'svhome/index.html', {})