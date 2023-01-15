from django.shortcuts import render
from .models import Category, Album, Image

# Create your views here.

# def categoryPage(request, slug):

#     category = Category.objects.get(slug=slug)
#     images = Image.objects.filter(category=category).order_by('-date_created')[:6]

#     for x in images:
#         x.shortDescription = x.description[:130]
    
#     context = {}
#     context['images'] = images
#     context['category'] = category

#     return render(request, 'gallery.html', context)

# def imageDetailPage(request, slug1, slug2):

#     category = Category.objects.get(slug=slug1)
#     image = Image.objects.get(slug=slug2)

#     context = {}
#     context['category'] = category
#     context['image'] = image

#     return render(request, 'main/image.html', context)

def categoryPage(request):

    category = Category.objects.all()

    return render(
        request, 
        'category.html',
        {
            'categories': category
        }
        )

def albumPage(request, tag):

    category_id = Category.objects.filter(tag=tag).values('id')
    album = Album.objects.filter(category_id__in=category_id)

    return render(
        request, 
        'album.html',
        {
            'albums': album,
        }
        )

def imagePage(request, pk):

    image = Album.objects.get(pk=pk)

    return render(
        request, 
        'image.html',
        {
            'images': image,
        }
        )