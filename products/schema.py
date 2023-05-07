from ninja import ModelSchema, Schema

from .models import Product, Size


class SizeSchema(ModelSchema):
    class Config:
        model = Size
        model_fields = '__all__'


class ColorSchema(ModelSchema):
    # need to define available
    class Config:
        model = Product
        model_fields = ('id', 'title', 'photo_main', 'slug')


class ProductListSchema(ModelSchema):
    # need to define available
    # url, discount_percents
    class Config:
        model = Product
        model_fields = ('id', 'slug', 'title', 'price', 'discount_price',
                  'photo_main', 'photo_1')


class ProductDetailSchema(ModelSchema):
    # is_favorite_product = serializers.SerializerMethodField()
    # is_in_cart = serializers.SerializerMethodField()
    # discount_percent = serializers.SerializerMethodField()
    # available = serializers.SerializerMethodField()
    # colors = ColorSerializer(many=True)
    # sizes = SizeSerializer(many=True)
    # default_size = serializers.SerializerMethodField()
    class Config:
        model = Product
        model_fields = '__all__'
