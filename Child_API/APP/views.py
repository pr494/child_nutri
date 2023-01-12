from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken, TokenAuthentication
from .serializers import RegisterSerializer,ChildrenSerializer,MDataSerializer,ADataSerializer
from .models import manual,auto
import json
@api_view(['POST'])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    return Response({
        'data':{
            'id':user.id,
            'username':user.username,
            'email':user.email,
        },
        
    })

@api_view(['GET'])
def get_user(request):
    user = request.user
    if user.is_authenticated:
        return Response({
            'data':{
            'id':user.id,
            'username':user.username,
            'email':user.email
        },
    })
    return Response({'error':'not authenticated'})

@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        _, token = AuthToken.objects.create(user)
        return Response({
            "data":{
            'id':user.id,
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "token": token
            },
            
        })

def serialize_child(child):
    return{
            "child_info":{
            "id":child.id,
            "User_id": child.User_id,
            "First_name": child.First_name,
            "Last_name": child.Last_name,
            "Gender": child.Gender,
            "date_of_birth": child.date_of_birth,
            "Organization": child.Organization,
            "Father_name": child.Father_name,
            "Father_mobile": child.Father_mobile,
            "Mother_name": child.Mother_name,
            "State": child.State,
            "District": child.District,
            "Taluk": child.Taluk,
            "Village": child.Village

            },
    }
        
@api_view(['POST'])
def ADD_CHILD(request):
    serializer = ChildrenSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        child = serializer.save()
        return Response(serialize_child(child))


@api_view(['GET'])
def get_child(request):
    Child = child.objects.all()
    serialize= ChildrenSerializer(Child,many=True)
    return Response(serialize.data)

    
@api_view(['POST'])
def ADD_mDATA(request):
    serializer = MDataSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        mdata = serializer.save()
        return Response({
            "child_Data":{
            'child_id':mdata.child_id,
            'Date':mdata.Date,
            'Manual_height':mdata.Manual_height,
            'Manual_weight':mdata.Manual_weight

            },

        })

@api_view(['POST'])
def ADD_aDATA(request):
    serializer = ADataSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        adata = serializer.save()
        return Response({
            "child_Data":{
            'child_id':adata.child_id,
            'Date':adata.Date,
            'Auto_height':adata.Auto_height,
            'Auto_weight':adata.Auto_weight

            },

        })

@api_view(['GET'])
def get_data(request):
    Data =auto.objects.all()
    serialize= ADataSerializer(Data,many=True)
    return Response(serialize.data)
    
    