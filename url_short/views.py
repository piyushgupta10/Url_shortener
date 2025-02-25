from django.shortcuts import render
from django.http import JsonResponse
from .models import ShortURL
import random
import string

# Create your views here.
def shorten_url(request):
    """API to shorten a URL"""
    if request.method == "POST":
        original_url = request.POST.get('url')
        short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

        # Save to the database
        short_url = ShortURL.objects.create(original_url=original_url, short_code=short_code)
        return JsonResponse({"shortened_url": request.build_absolute_uri(f"/{short_code}")})

    return render(request, "urls_app/index.html")
