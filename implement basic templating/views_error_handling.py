from rest_framwork.decorators import api_view
from rest_framwork.response import Response
from rest_framwork import status 
from django.db import DatabaseError
from .models import Customer
from .serializers import CustomerSerializer

@api_view(['GET'])
def get_customers(request):
    try:
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        except DatabaseError as e:
            return Response(
                {"error": "Databse error occurred","details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            except Exception as e:
                return Response(
                    {"error": "An unexpected error occurred", "details": str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )