from django.shortcuts import render


def index(request):
    """Главная страница."""
    template = 'index.html'
    return render(request, template)
