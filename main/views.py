from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def show_main(request: HttpRequest) -> HttpResponse:
    context = {
        'name': 'Juan Maxwell Tanaya',
        'class': 'C',
        'inventory': [
            {
                'name': 'Traveler\'s Guide',
                'amount': 163,
            },
            {
                'name': 'Refined Aether',
                'amount': 123,
            },
            {
                'name': 'Lost Crytsal',
                'amount': 321,
            }
        ]
    }

    return render(request, "main.html", context)
