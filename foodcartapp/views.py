from django.http import JsonResponse
from django.templatetags.static import static
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product, Customer, Order


def banners_list_api(request):
    # FIXME move data to db?
    return JsonResponse([
        {
            'title': 'Burger',
            'src': static('burger.jpg'),
            'text': 'Tasty Burger at your door step',
        },
        {
            'title': 'Spices',
            'src': static('food.jpg'),
            'text': 'All Cuisines',
        },
        {
            'title': 'New York',
            'src': static('tasty.jpg'),
            'text': 'Food is incomplete without a tasty dessert',
        }
    ], safe=False, json_dumps_params={
        'ensure_ascii': False,
        'indent': 4,
    })


def product_list_api(request):
    products = Product.objects.select_related('category').available()

    dumped_products = []
    for product in products:
        dumped_product = {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'special_status': product.special_status,
            'description': product.description,
            'category': {
                'id': product.category.id,
                'name': product.category.name,
            } if product.category else None,
            'image': product.image.url,
            'restaurant': {
                'id': product.id,
                'name': product.name,
            }
        }
        dumped_products.append(dumped_product)
    return JsonResponse(dumped_products, safe=False, json_dumps_params={
        'ensure_ascii': False,
        'indent': 4,
    })


@api_view(['POST'])
def register_order(request):
    order = request.data
    product_error_content = {'error': 'products are non presented or not list'}
    try:
        product_check = isinstance(order['products'], list)
        if not product_check or len(order['products']) == 0:
            return Response(product_error_content,
                            status=status.HTTP_404_NOT_FOUND)
    except KeyError:
        return Response(product_error_content,
                        status=status.HTTP_404_NOT_FOUND)
    customer = Customer.objects.create(
                            first_name=order['firstname'],
                            last_name=order['lastname'],
                            phone=order['phonenumber'],
                            address=order['address'])
    for product in order['products']:
        Order.objects.create(customer=customer,
                             product=Product.objects.get(id=product
                                                         ['product']),
                             count=product['quantity'])
    return Response({})
