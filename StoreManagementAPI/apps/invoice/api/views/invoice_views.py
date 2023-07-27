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
                'date': None,
                'subtotal': subtotal, 
                'discount': discount,
                'total': subtotal - discount,
                'paid_with': data['paid_with'],
                'change': data['paid_with'] - total
            }
            soh_serializer = SalesOrderHeaderSerializer(data=sales_order_header_body)
            if soh_serializer.is_valid():
                soh = soh_serializer.save()
            
            
            
            return Response({'hola': soh.id})
            
            #Ingresar los datos en SalesOrderHeader
            #subtotal = models.DecimalField("Subtotal", max_digits=10, decimal_places=4, null=False, blank=False)
            #discount = 0
            #total = subtotal - discount
            #paid_with = 
            #change = paid_with - total
            
            #Ingresar los datos en SalesOrderDetail
            #sales_order_header = salesOrderHeader.id
            #product = sales_data.id_product
            #price = sales_data.product_price
            #quantity = sales_data.quantity
            #discount = 0
            
            
            #Restar la cantidad de productos que se compraron
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

