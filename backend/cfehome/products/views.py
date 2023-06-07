from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer

class ProductCreateAPIView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def perform_create(self, serializer):
#        serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content')or None
        if content is None:
            content=title
        serializer.save(content=content)

product_list_create_view=ProductCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

product_detail_view=ProductDetailAPIView.as_view()

@api_view(['GET','POST'])
def product_alt_view(request,pk=None,*args,**kwargs):
    method=request.method

    if method=="GET":

        #list_view
        if pk==None:
            queryset=Product.objects.all()
            data=ProductSerializer(queryset,many=True).data
            return Response(data)
        
        queryset=Product.objects.filter(pk=pk)

        obj=get_object_or_404(Product,pk=pk)
        data=ProductSerializer(obj,many=False).data
        return Response(data)

    if method=="POST":
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title=serializer.validated_data.get('title')
            content=serializer.validated_data.get('content')or None
            if content is None:
                content=title
            serializer.save(content=content)
        return Response(serializer.data)
    return Response({"invalid":"not good data"})    

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer 
    lookup_field='pk'

    def perform_update(self,serializer):
        instance=serializer.save()
        if not instance.content:
            instance.content=instance.title

update_detail_view=ProductUpdateAPIView.as_view()

class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer 
    lookup_field='pk'

    def perform_destroy(self,instance):
        super().perform_destroy(instance)

product_destroy_view=ProductDestroyAPIView.as_view()