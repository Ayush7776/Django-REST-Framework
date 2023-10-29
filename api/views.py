from .models import Student
from .serializer import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly

# Create your views here.
class StudetModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
    authentication_classes=[SessionAuthentication]
    # This Will Be Only Take Permission To Staff Status True In Admin Panel
    # permission_classes=[IsAuthenticated]

    # In AllowAny  Can Make Operation Authenticated Or NonAuthenticated User 
    # permission_classes=[AllowAny]

    # IsAdminUser Admin Can Make Operation And All User Cannot Access API Data 
    # permission_classes=[IsAdminUser]

    # In IsAuthenticatedOrReadOnly Authenticated User Can Make Operation And    UnAuthenticated User Can Read Only API Data 
    # permission_classes=[IsAuthenticatedOrReadOnly]

    # In DjangoModelPermissions We Have To Explicitly Take Permission From SuperUser Pannel
    # permission_classes=[DjangoModelPermissions]

    # In DjangoModelPermissionsOrAnonReadOnly We Have To Explicitly Take Permission From SuperUser Pannel And UnAuthorized User Can Read Only
    # permission_classes=[DjangoModelPermissionsOrAnonReadOnly]


    