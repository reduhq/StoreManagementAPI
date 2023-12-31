from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework import viewsets
from rest_framework import generics
from apps.invoice.api.serializers.invoice_serializers import (
    SalesOrderSerializer,
    SalesOrderHeaderSerializer,
    SalesOrderDetailSerializer, 
    SalesOrderHeaderOutSerializer
)
from django.db.models import Prefetch
from drf_yasg.utils import swagger_auto_schema
from apps.product.models import Product
from apps.product.api.serializers.product_serializer import ProductSerializer
from apps.invoice.models import SalesOrderHeader, SalesOrderDetail    

class InvoiceView(viewsets.GenericViewSet):
    def calculate_subtotal(self, sales_data) -> float:
        return sum(sale['quantity']*sale['product_price'] for sale in sales_data)
    
    # POST Method
    @swagger_auto_schema(  
        request_body=SalesOrderSerializer, # Especifica el serializador del cuerpo de la solicitud (input)
        responses={
            status.HTTP_200_OK: SalesOrderHeaderOutSerializer  # Formato de la respuesta (output)
            # status.HTTP_400_BAD_REQUEST: "{'error': 'Mensaje de error'}",  # Respuesta en caso de error de validación
        }
    )
    def create(self, request):
        try:
            # Extracting the data from 'request'
            data = request.data
            request_serializer = SalesOrderSerializer(data=data)
            if not request_serializer.is_valid():
                raise ValidationError()
            
            # If the information is valid
            # create a register in SalesOrderHeader
            subtotal = self.calculate_subtotal(request_serializer.data['sales_data'])
            discount = 0
            total = subtotal - discount
            paid_with = request_serializer.data['paid_with']
            
            sales_order_header_body = {
                'subtotal': subtotal, 
                'discount': discount,
                'total': subtotal - discount,
                'paid_with': paid_with,
                'change': paid_with - total
            }
            soh_serializer = SalesOrderHeaderSerializer(data=sales_order_header_body)
            soh_serializer.is_valid(raise_exception=True) # If the data is not valid, raise an e exception
            soh = soh_serializer.save()
            
            # Creating a register in SalesOrderDetail
            sod_data = [{
                'sales_order_header': soh.id,
                'product': obj['id_product'],
                'price': obj['product_price'],
                'quantity': obj['quantity'],
                'subtotal': obj['product_price'] * obj['quantity'],
                'discount': 0,
                'total': obj['product_price'] * obj['quantity']
            } for obj in request_serializer.data['sales_data']]
            
            sod_serializer = SalesOrderDetailSerializer(data=sod_data, many=True)
            sod_serializer.is_valid(raise_exception=True) # If the data is not valid, raise an e exception
            sod = sod_serializer.save()
            
            # Subtract the number of products that were sold
            for obj in request_serializer.data['sales_data']:
                product = Product.objects.get(id = obj['id_product']) # Get the element to update
                obj_update = {'quantity': product.quantity - obj['quantity']}
                
                prod_serializer = ProductSerializer(product, data=obj_update, partial=True)
                prod_serializer.is_valid(raise_exception=True) # If the data is not valid, raise an e exception
                # Perform Update
                prod_serializer.save()
            
            # Creating the Response data
            response_data = SalesOrderHeader.objects.get(id = soh_serializer.data['id'])
            response_serializer = SalesOrderHeaderOutSerializer(response_data)
            
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
            
        except ValidationError as e:
            return Response({'errors': prod_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    # GET Method
    @swagger_auto_schema(  
        # request_body=MiModeloSerializer, # Especifica el serializador del cuerpo de la solicitud (input)
        responses={
            status.HTTP_200_OK: SalesOrderHeaderOutSerializer  # Formato de la respuesta (output)
            # status.HTTP_400_BAD_REQUEST: "{'error': 'Mensaje de error'}",  # Respuesta en caso de error de validación
        }
    )
    def list(self, request):
        queryset = SalesOrderHeader.objects.all()
        serializer = SalesOrderHeaderSerializer(queryset, many=True)
        return Response(serializer.data)

