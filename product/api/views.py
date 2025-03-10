from product.models import ProductCategory, Product, ProductTag
from django.http import JsonResponse
from product.api.serializers import CategorySerializer, ProductSerializer, ProductCreateSerializer, TagSerializer
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class CategoryApiView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = ProductCategory.objects.all()


class TagApiView(ListAPIView):
    serializer_class = TagSerializer
    queryset = ProductTag.objects.all()


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


@api_view(http_method_names = ['GET', 'POST'])
def products(request):
    if request.method == 'POST':
        serializer = ProductCreateSerializer(data = request.data, context = {'request' : request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe = False, status = 201)
        return JsonResponse(data=serializer.errors, safe = False, status = 400)
    products = Product.objects.all()
    serializer = ProductSerializer(products, context = {'request': request}, many = True)
    return JsonResponse(data = serializer.data, safe = False)


@api_view(http_method_names = ['PUT', 'PATCH'])
def product_update(request, pk):
    product = Product.objects.get(id = pk)
    if request.method == 'PUT':
        serializer = ProductCreateSerializer(data = request.data, context = {'request' : request}, instance = product)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe = False, status = 201)
        return JsonResponse(data=serializer.errors, safe = False, status = 400)
    if request.method == 'PATCH':
        serializer = ProductCreateSerializer(data = request.data, context = {'request' : request}, instance = product, partial = True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe = False, status = 201)
        return JsonResponse(data=serializer.errors, safe = False, status = 400)
    products = Product.objects.all()
    serializer = ProductSerializer(products, context = {'request': request}, many = True)
    return JsonResponse(data = serializer.data, safe = False)


class ProductListApiView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProductCreateSerializer
        return self.serializer_class
    

class ProductRetrieveUpdateView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductCreateSerializer
    queryset = Product.objects.all()