from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.db.models import Q
from .models import User, Contact, Spam
from .serializers import UserSeri,SpamSeri, ContactSeri, SearchSeri
from django.http import HttpResponse

def home(request):
    details = (
        "LOGIN PAGE >>>> "
        'admin panel (username and password are admin) - /admin/ ,\n'
        'register page - /api/register/ ,\n'
        'login - /api/login/ ,\n'
        'search - /api/search/?q= ,\n'
        'user detail - /api/user-detail/<str:phone_number>/'
    )
    return HttpResponse(details)

@api_view(['POST'])
@permission_classes([AllowAny])
def registryView(request):
    serializer=UserSeri(data=request.data)
    if serializer.is_valid():
        user=serializer.save()
        return Response({'message':'user registered!','user': UserSeri(user).data,}, status=201)
    return Response(serializer.errors,status=400)


@api_view(['POST'])
@permission_classes([AllowAny])
def LoginView(request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username= username, password=password)
        
        if user:
            token,created = Token.objects.get_or_create(user=user)
            return Response({'token':token.key,'user': UserSeri(user).data,},status=201)
        return Response({'error!':"Invalid Creds"}, status=400)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def SpamView(request):
    serializer = SpamSeri(data=request.data)
    if serializer.is_valid():
        serializer.save(reporter=request.user)
        return Response({'message':'Spam!'},status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def SearchView(request):
    quest =request.query_params.get('q','').strip()
    if quest:
        users =User.objects.filter(
          Q(username__icontains=quest) | Q(phone__icontains=quest)
        )
    else:
        users= User.objects.none()
        
    serializer = SearchSeri(users,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_detail(request, phone_number):
    try:
          user = User.objects.get(phone=phone_number)
    except User.DoesNotExist:
         return Response({'error!':'User not found!'},status=404)
    
    serializer=UserSeri(user)
    return Response(serializer.data)

