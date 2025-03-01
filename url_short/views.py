from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.utils.timezone import now
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
def redirect_url(request, short_code):
    """Redirect short URL to the original URL"""
    short_url = get_object_or_404(ShortURL, short_code=short_code)

    # Check if the URL has expired
    if short_url.expires_at and short_url.expires_at < now():
        return JsonResponse({"error": "This link has expired"}, status=410)

    return redirect(short_url.original_url)
