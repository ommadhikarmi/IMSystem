
from django.urls import path
from.views import ResourceTypeView
from.views import DepartmentView
from.views import ResourcesView
from.views import VendorView
from.views import PurchaseView
from.views import Register
from.views import Login


from.views import ResourceTypeDetailView
from.views import DepartmentDetailView
from.views import ResourcesViewDetail
from.views import VendorViewDetail
from.views import PurchaseViewDetail

urlpatterns = [
    path('resource_type/',ResourceTypeView.as_view()),
    path('resource_type/<int:pk>/',ResourceTypeDetailView.as_view()),

    path('department/',DepartmentView.as_view()),
    path('department/<int:pk>/',DepartmentDetailView.as_view()),

    path('resources/',ResourcesView.as_view()),
    path('resources/<int:pk>/',ResourcesViewDetail.as_view()),

    path('vendor/',VendorView.as_view()),
    path('vendor/<int:pk>/',VendorViewDetail.as_view()),

    path('purchase/',PurchaseView.as_view()),
    path('purchase/<int:pk>/',PurchaseViewDetail.as_view()),

    path('register/',Register), # why not as_view because this is function class based view
    path('login/',Login) # why not as_view because this is function class based view


]