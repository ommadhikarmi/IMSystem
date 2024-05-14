from django.shortcuts import render
from django.contrib .auth import authenticate
from django.contrib .auth .hashers import make_password

from .models import ResourceType
from .models import Department
from .models import Resources
from .models import Vendor
from .models import Purchase

from .serializers import ResourceTypeSerializer
from .serializers import DepartmentSerializer
from .serializers import ResourcesSerializer
from .serializers import VendorSerializer
from .serializers import PurchaseSerializer
from .serializers import UserSerializer

from rest_framework .generics import GenericAPIView
from rest_framework .response import Response
from rest_framework import status
from rest_framework .decorators import api_view  # why this because we are using function based view
from rest_framework .authtoken.models import Token
from rest_framework .decorators import permission_classes
from rest_framework .permissions import AllowAny, DjangoModelPermissions

 

# Create your views here.

class ResourceTypeView(GenericAPIView):
    queryset = ResourceType.objects.all()
    serializer_class = ResourceTypeSerializer

    #get method which shows json data into list
    def get(self,request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data)
    
    #post method which create data
    def post(self,request):
        data = request.data
        serializer =self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response('Data is created!')
        else:
            return Response(serializer.errors)

 # if id is pass then use pk and create new class because get method is already used in above code.       
class ResourceTypeDetailView(GenericAPIView):
    queryset = ResourceType.objects.all()
    serializer_class = ResourceTypeSerializer

    def get(self,request,pk):
        try:
            resourcetype_obj =ResourceType.objects.get(id=pk)
        except:
            return Response('Data not found',status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(resourcetype_obj)
        return Response(serializer.data)
    
    # put method is used to update data
    def put(self,request,pk):
        try:
            resourcetype_obj =ResourceType.objects.get(id=pk)
        except:
            return Response('Data not found',status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(resourcetype_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('data updated!')
        else:
            return Response(serializer.errors)
    # delete method is used to delete data    
    def delete(self,request,pk):
        try:
            resourcetype_obj =ResourceType.objects.get(id=pk)
        except:
            return Response('Data not found',status=status.HTTP_404_NOT_FOUND)
        resourcetype_obj.delete()
        return Response('data deleted!')

#  ----------------End of ResourceTypeViews----------------------

class DepartmentView(GenericAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get(self,request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data)
    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)  
        if serializer.is_valid():
            serializer.save()
            return Response('department is created')
        else:
            return Response(serializer.errors)  

class DepartmentDetailView(GenericAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer 
    
    def get(self,request,pk):  #  <--retrieve method
        try:
            department_obj = Department.objects.get(id=pk)
        except:
            return Response('Department not found!',status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(department_obj)
        return Response(serializer.data)
    def put(self,request,pk):  #  <--update/edit method
        try:
            department_obj = Department.objects.get(id=pk)
        except:
            return Response('Department not found!',status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(department_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Department is updated!')
        else:
            return Response(serializer.errors)
    def delete(self,request,pk):
        try:
            department_obj = Department.objects.get(id=pk)
        except:
            return Response('Department not found!',status=status.HTTP_404_NOT_FOUND)
        department_obj.delete()
        return Response('deleted')
    #--------------------- End of Department View-----------

class ResourcesView(GenericAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResourcesSerializer
    filterset_fields = ['type','departments']
    search_fields =['name']


    def get(self,request):
        queryset = self.get_queryset()
        filtered_queryset = self.filter_queryset(queryset)
        serializer = self.serializer_class(filtered_queryset,many=True) # filtered_queryset lay naii search gardinxa
        return Response(serializer.data)
    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response('Resource is created!')
        else:
            return Response(serializer.errors)
        
class ResourcesViewDetail(GenericAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResourcesSerializer
    
    def get(self,request,pk):
        try:
            Resources_obj = Resources.objects.get(id=pk)
        except:
            return Response('resources not found',status=status.HTTP_404_NOT_FOUND)
        serializer =self.serializer_class(Resources_obj)
        return Response(serializer.data)
    def put(self,request,pk):
        try:
            Resources_obj = Resources.objects.get(id=pk)
        except:
            return Response('resources not found',status=status.HTTP_404_NOT_FOUND)
        serializer =self.serializer_class(Resources_obj,data=request.data)
        if serializer.isvalid():
            serializer.save()
            return Response('Resources is updated!')
            
        else:
            return Response('Resources not found')
    def delete(self,request,pk):
        try:
            Resources_obj = Resources.objects.get(id=pk)
        except:
            return Response('resources not found',status=status.HTTP_404_NOT_FOUND)
        Resources_obj.delete()
        return Response('Resources data deleted!')
#---------------- End of Resources View-----------------

class VendorView(GenericAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def get(self,request):
        queryset = self.get_queryset() 
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data)
    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response('Vendor data is created!')
        else:
            return Response(serializer.errors)
        
class VendorViewDetail(GenericAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def get(self,request,pk):
        try:    
            Vendor_obj = Vendor.objects.get(id=pk)
        except: 
            return Response('Vendor data not found',status=status.HTTP_404_NOT_FOUND)   
        serializer = self.serializer_class(Vendor_obj)
        return Response(serializer.data)
    def put(self,request,pk):
        try:    
            Vendor_obj = Vendor.objects.get(id=pk)
        except: 
            return Response('Vendor data not found',status=status.HTTP_404_NOT_FOUND)       
        serializer = self.serializer_class(Vendor_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Vendor data is updated/edited!')
        else:
            return Response(serializer.errors)
    def delete(self,request,pk):
        try:    
            Vendor_obj = Vendor.objects.get(id=pk)
        except: 
            return Response('Vendor data not found',status=status.HTTP_404_NOT_FOUND)
        Vendor_obj.delete()
        return Response('Vendor data deleted!')
#  ===================End of Vendor View========================    

class PurchaseView(GenericAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

    def get(self,request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data)
    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response('purchased!')
        else:
            return Response(serializer.errors)
        
class PurchaseViewDetail(GenericAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

    def get(self,request,pk):
        try:
            Purchase_obj = Purchase.objects.get(id=pk)
        except:
            return Response('not purchased!',status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(Purchase_obj)
        return Response(serializer.data)
    def put(self,request,pk):
        try:
            Purchase_obj = Purchase.objects.get(id=pk)
        except:
            return Response('not purchased!',status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(Purchase_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('data is updated!')
        else:
            return Response(serializer.errors)
        
    def delete(self,request,pk):
        try:
            Purchase_obj = Purchase.objects.get(id=pk)
        except:
            return Response('not purchased!',status=status.HTTP_404_NOT_FOUND)
            Purchase_obj.delete()
            return Response('data is deleted!')
        

@api_view(['POST'])
def Register(request):
    password = request.data.get('password')
    hash_password = make_password(password)
    request.data['password'] = hash_password
    serializer = UserSerializer(data=request.data) 
    if serializer.is_valid():
        serializer.save()
        return Response('User created!')
    else:
        return Response(serializer.errors) 

@api_view(['POST'])
@permission_classes([AllowAny]) # In login all user can request 
def Login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(username=email,password=password)
    if user == None:
        return Response('Email or password is Invalid',status=status.HTTP_400_BAD_REQUEST)
    else:
        token,_ = Token.objects.get_or_create(user=user)
        return Response(token.key) # token =>object of token model,key =>attributes which stores value

    





        
    
    
    

    
    
        
