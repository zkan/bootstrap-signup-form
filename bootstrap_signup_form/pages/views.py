from django.contrib import messages
from django.shortcuts import render
from django.views import View

from .models import Lead


class IndexView(View):
    def get(self, request):
        return render(
            request,
            'index.html'
        )

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        country = request.POST.get('country')

        Lead.objects.create(
            name=name,
            email=email,
            country=country
        )

        messages.success(request, 'Thank you for signing up!')

        return render(
            request,
            'index.html'
        )
