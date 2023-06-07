import json
from django.forms.models import model_to_dict
from django.http import JsonResponse,HttpResponse
from products.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer
from django.http import JsonResponse

# Create your views here.
@api_view(["POST"])
def api_home(request,*args,**kwargs):
#     instance=Product.objects.all().order_by("?").first()
#     data={}
#     if instance:
#  #       data=model_to_dict(instance,fields=['id','title','price','sale_price'])
#         data=ProductSerializer(instance).data
#    data=request.data
    serializer=ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance=serializer.save()
        print(instance)
        return Response(serializer.data)
 #   return Response({"invalid":"not good data"},status=400)