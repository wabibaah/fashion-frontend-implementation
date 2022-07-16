import random
from django.shortcuts import render
from store.models import Product, ReviewRating

def home(request):
  products = Product.objects.all().filter(is_available=True).order_by('created_date') #remember - later

  reviews = 0  ### causing problems but made me learn about database migrations on the server

  is_featured = products.filter(is_featured = True)

  for product in products:
    reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

  trending_products = list(Product.objects.all().filter(is_available=True).order_by('id'))
  if len(trending_products) >= 6:
    trending_products = random.sample(trending_products, 6)
  trending_products1 = trending_products[:3]
  trending_products2 = trending_products[3:]

  top_rated_products = list(Product.objects.all().filter(is_available=True).order_by('id'))
  if len(top_rated_products) >= 6:
    top_rated_products = random.sample(top_rated_products, 6)
  top_rated_products1 = top_rated_products[:3]
  top_rated_products2 = top_rated_products[3:]

  latest_products = list(Product.objects.all().filter(is_available=True).order_by('-id'))
  latest_products1 = latest_products[:3]
  latest_products2 = latest_products[3:6]

  context = {
    'products': products,
    'reviews': reviews,
    'is_featured': is_featured,
    'trending_products1': trending_products1,
    'trending_products2': trending_products2,
    'latest_products1': latest_products1,
    'latest_products2': latest_products2,
    'top_rated_products1': top_rated_products1,
    'top_rated_products2': top_rated_products2,
  }
  return render(request, 'home.html', context)





### products is got from the database which is original in django (not mongodb) 
### the context is just so that we can pass information about the products into the home page
### the home page is handled by the greatkart (main) view.py file and I don't know why
### the data is got from the views.py file and that same views.py file gives the data to the home.html template in the template folder