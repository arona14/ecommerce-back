from django.shortcuts import get_object_or_404
from ninja import Router
from typing import List
from .models import Product
from .schema import ProductListSchema, ProductDetailSchema


router = Router()



@router.get("/", response=List[ProductListSchema])
def get_rules(request):
    queryset = Product.objects.all()
    return queryset

@router.get("/{slug}", response=ProductDetailSchema)
def get_rule(request, slug: str):
    rule = get_object_or_404(Product, slug=slug)
    return rule
