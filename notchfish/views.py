from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .models import Product

def home(request):
    products = Product.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'home.html', {'products': products})