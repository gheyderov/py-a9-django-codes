from product.models import ProductCategory, Product
from django.http import JsonResponse
from product.api.serializers import CategorySerializer, ProductSerializer


def categories(request):
    categories = ProductCategory.objects.all()
    serializer = CategorySerializer(categories, many = True)
    # category_dict = []
    # for category in categories:
    #     if category.parent:
    #         category_dict.append({
    #             'parent_id' : category.parent.id,
    #             'parent_title' : category.parent.title,
    #             'cat_id' : category.id,
    #             'title' : category.title
    #         })
    #     else:
    #         category_dict.append({
    #             'cat_id' : category.id,
    #             'title' : category.title
    #         })
    return JsonResponse(data = serializer.data, safe = False)


def products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, context = {'request': request}, many = True)
    return JsonResponse(data = serializer.data, safe = False)