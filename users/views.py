from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response

from users.serializers import UserSerializer ,CustomTokenObtainPairSerializer

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
# Create your views here.

class UserView(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'가입완료'},status=status.HTTP_201_CREATED)
        else:
            return Response({'message':f'${serializer.errors}'},status=status.HTTP_400_BAD_REQUEST) 

# jwt공식문서 참조 (커스텀마이징)
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    

# login 확인 하는 함수
class mockView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        return Response("get response")
    
    def post(self,requst):
        user = requst.user
        user.is_admin =True
        user.save()
        return Response("어드민 유저로 변경")