from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework import viewsets
from rest_framework import generics
from apps.invoice.api.serializers.invoice_serializers import (
    SalesOrderSerializer,
    SalesOrderHeaderSerializer,
    SalesOrderDetailSerializer, 
)
from drf_yasg.utils import swagger_auto_schema
from apps.product.models import Product
from apps.product.api.serializers.product_serializer import ProductSerializer
from apps.invoice.models import SalesOrderHeader, SalesOrderDetail    

class InvoiceView(viewsets.GenericViewSet):
    serializer_class = SalesOrderSerializer
    
    def calculate_subtotal(self, sales_data) -> float:
        return sum(sale['quantity']*sale['product_price'] for sale in sales_data)
    
    # POST Method
    def create(self, request):
        try:
            # Extracting the data from 'request'
            data = request.data
            validation = self.get_serializer(data=data)
            if not validation.is_valid():
                raise ValidationError()
            
            # If the information is valid
            # create a register in SalesOrderHeader
            subtotal = self.calculate_subtotal(data['sales_data'])
            discount = 0
            total = subtotal - discount
            
            sales_order_header_body = {
                'subtotal': subtotal, 
                'discount': discount,
                'total': subtotal - discount,
                'paid_with': data['paid_with'],
                'change': data['paid_with'] - total
            }
            soh_serializer = SalesOrderHeaderSerializer(data=sales_order_header_body)
            if soh_serializer.is_valid():
                soh = soh_serializer.save()
            
            # Creating a register in SalesOrderDetail
            sod_data = []
            for obj in validation.data['sales_data']:
                if not Product.objects.filter(id = obj['id_product']): 
                    raise ValidationError()
                obj_in = {
                    'sales_order_header': soh.id,
                    'product': obj['id_product'],
                    'price': obj['product_price'],
                    'quantity': obj['quantity'],
                    'discount': 0
                }
                sod_data.append(obj_in)
            
            sod_serializer = SalesOrderDetailSerializer(data=sod_data, many=True)
            if sod_serializer.is_valid():
                sod = sod_serializer.save()
                
            
            # Subtract the number of products that were sold
            for obj in validation.data['sales_data']:
                product = Product.objects.filter(id = obj['id_product']).first()
                obj_update = {
                    'quantity': product.quantity - obj['quantity']
                }
                prod_serializer = ProductSerializer(product, data=obj_update, partial=True)
                prod_serializer.is_valid(raise_exception=True)
                # Perform Update
                prod_serializer.save()
            
            return Response({'hola': SalesOrderDetailSerializer(sod, many=True).data})
            
        except ValidationError as e:
            return Response({'errors': validation.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    # GET Method
    @swagger_auto_schema(  
        # request_body=MiModeloSerializer, # Especifica el serializador del cuerpo de la solicitud (input)
        responses={
            status.HTTP_200_OK: SalesOrderHeaderSerializer  # Formato de la respuesta (output)
            # status.HTTP_400_BAD_REQUEST: "{'error': 'Mensaje de error'}",  # Respuesta en caso de error de validación
        }
    )
    def list(self, request):
        queryset = SalesOrderHeader.objects.all()
        serializer = SalesOrderHeaderSerializer(queryset, many=True)
        return Response(serializer.data)

