from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'products/index.html')


def products(request):
    context = {
        'title': 'Test title',
        'products':[
            {'name': 'Худи черногоцвета цвета', 'price': 1050},
            {'name': 'Джинсы', 'price': 750},
            {'name': 'Футболка', 'price': 105},

        ]
    }
    return render(request, 'products/products.html', context)
