from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Bank, Branch
from .serializers import (
    BankSerializer, 
    BankWithBranchesSerializer,
    BranchListSerializer, 
    BranchDetailSerializer
)


class BankListView(generics.ListAPIView):
    """
    List all banks.
    
    Returns a paginated list of all banks in the system.
    """
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class BankDetailView(generics.RetrieveAPIView):
    """
    Retrieve a specific bank.
    
    Returns detailed information about a specific bank by ID.
    """
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    lookup_field = 'id'


class BankBranchesView(generics.ListAPIView):
    """
    List all branches for a specific bank.
    
    Returns a paginated list of all branches belonging to a specific bank.
    """
    serializer_class = BranchListSerializer
    
    def get_queryset(self):
        bank_id = self.kwargs['bank_id']
        return Branch.objects.filter(bank_id=bank_id).select_related('bank')


class BranchListView(generics.ListAPIView):
    """
    List all branches.
    
    Returns a paginated list of all branches in the system with basic information.
    """
    queryset = Branch.objects.select_related('bank').all()
    serializer_class = BranchListSerializer


class BranchDetailView(generics.RetrieveAPIView):
    """
    Retrieve a specific branch.
    
    Returns detailed information about a specific branch by ID, including bank details.
    """
    queryset = Branch.objects.select_related('bank').all()
    serializer_class = BranchDetailSerializer
    lookup_field = 'id'


@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter('ifsc', openapi.IN_QUERY, description="Search by IFSC code", type=openapi.TYPE_STRING),
        openapi.Parameter('city', openapi.IN_QUERY, description="Search by city name", type=openapi.TYPE_STRING),
    ],
    responses={
        200: openapi.Response(
            description="Search results",
            examples={
                "application/json": {
                    "branch": {
                        "id": 1,
                        "name": "Mumbai Main Branch",
                        "ifsc": "SBIN0000001",
                        "address": "123 Fort Area, Mumbai",
                        "city": "Mumbai",
                        "state": "Maharashtra",
                        "bank": {
                            "id": 1,
                            "name": "State Bank of India",
                            "code": "SBI"
                        }
                    }
                }
            }
        ),
        400: "Bad Request - Missing search parameters",
        404: "Not Found - No branches found"
    }
)
@api_view(['GET'])
def branch_search(request):
    """
    Search branches by IFSC code or city.
    
    Search for branches using either IFSC code (exact match) or city name (partial match).
    At least one search parameter (ifsc or city) must be provided.
    """
    ifsc = request.GET.get('ifsc')
    city = request.GET.get('city')
    
    if not ifsc and not city:
        return Response(
            {'error': 'Please provide either ifsc or city parameter'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    queryset = Branch.objects.select_related('bank')
    
    if ifsc:
        queryset = queryset.filter(ifsc__iexact=ifsc)
    elif city:
        queryset = queryset.filter(city__icontains=city)
    
    if not queryset.exists():
        return Response(
            {'message': 'No branches found'}, 
            status=status.HTTP_404_NOT_FOUND
        )
    
    # If searching by IFSC, return single result
    if ifsc:
        branch = queryset.first()
        serializer = BranchDetailSerializer(branch)
        return Response({'branch': serializer.data})
    
    # If searching by city, return list of results
    serializer = BranchListSerializer(queryset, many=True)
    return Response({'branches': serializer.data})


@swagger_auto_schema(
    method='get',
    responses={
        200: openapi.Response(
            description="API Overview",
            examples={
                "application/json": {
                    "Banks": {
                        "List all banks": "/api/banks/",
                        "Bank details": "/api/banks/{id}/",
                        "Bank branches": "/api/banks/{id}/branches/"
                    },
                    "Branches": {
                        "List all branches": "/api/branches/",
                        "Branch details": "/api/branches/{id}/",
                        "Search by IFSC": "/api/branches/search/?ifsc={ifsc_code}",
                        "Search by city": "/api/branches/search/?city={city_name}"
                    }
                }
            }
        )
    }
)
@api_view(['GET'])
def api_overview(request):
    """
    API overview endpoint.
    
    Returns a comprehensive list of all available API endpoints with their descriptions.
    """
    api_urls = {
        'Banks': {
            'List all banks': '/api/banks/',
            'Bank details': '/api/banks/{id}/',
            'Bank branches': '/api/banks/{id}/branches/'
        },
        'Branches': {
            'List all branches': '/api/branches/',
            'Branch details': '/api/branches/{id}/',
            'Search by IFSC': '/api/branches/search/?ifsc={ifsc_code}',
            'Search by city': '/api/branches/search/?city={city_name}'
        }
    }
    return Response(api_urls)
