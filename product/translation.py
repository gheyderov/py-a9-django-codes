from modeltranslation.translator import register, TranslationOptions
from product.models import ProductCategory

@register(ProductCategory)
class ProductCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)