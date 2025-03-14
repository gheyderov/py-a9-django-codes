from rest_framework import serializers
from product.models import ProductCategory, Product, ProductTag
from core.models import Subscriber


class SubscriberCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscriber
        fields = (
            'email',
        )


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductTag
        fields = (
            'id',
            'title'
        )


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = (
            'id',
            'parent',
            'title'
        )


class ProductSerializer(serializers.ModelSerializer):

    # category = serializers.CharField(source = 'category.title')
    category = CategorySerializer()
    tags = TagSerializer(many = True)

    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'description',
            'category',
            'tags',
            'cover_image',
            'price',
            'slug'
        )


class ProductCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'description',
            'category',
            'tags',
            'cover_image',
            'price',
            'slug'
        )