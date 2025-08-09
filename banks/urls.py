from django.urls import path
from . import views

urlpatterns = [
    # API overview
    path('', views.api_overview, name='api-overview'),
    
    # Banks endpoints
    path('banks/', views.BankListView.as_view(), name='bank-list'),
    path('banks/<int:id>/', views.BankDetailView.as_view(), name='bank-detail'),
    path('banks/<int:bank_id>/branches/', views.BankBranchesView.as_view(), name='bank-branches'),
    
    # Branches endpoints
    path('branches/', views.BranchListView.as_view(), name='branch-list'),
    path('branches/<int:id>/', views.BranchDetailView.as_view(), name='branch-detail'),
    path('branches/search/', views.branch_search, name='branch-search'),
]
