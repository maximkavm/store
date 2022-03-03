from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'products/index.html')


def products(request):
    context = {
        'title': 'Test title',
        'products': [
            {
                'name': 'Худи черного цвета с монограммами adidas Originals',
                'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
                'price': 6090
            },
            {
                'name': 'Синяя куртка The North Face',
                'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
                'price': 23725
            },
            {
                'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
                'price': 3390            },


        ]
    }
    return render(request, 'products/products.html', context)
