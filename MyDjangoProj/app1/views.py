from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from  rest_framework.serializers import Serializer
from app1.serializers import ManagerSerializer,LoginSerializer,EmployeeSerializer,LogoutSerializer
from rest_framework.generics import CreateAPIView,GenericAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView,UpdateAPIView
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Manager,Employee
from rest_framework import viewsets, status


class ManagerSignIn(GenericAPIView):
    serializer_class = ManagerSerializer

    def post(self, request):
        serializer = ManagerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            authentication_classes = [SessionAuthentication]
            permission_classes = [IsAuthenticated]

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MangerLogin(CreateAPIView):
    serializer_class = LoginSerializer


    def post(self, request, *args, **kwargs):
        ls=LoginSerializer(data=request.data)

        if ls.is_valid():
            try:
               manager= Manager.objects.get(email=ls.validated_data['email'],password=ls.validated_data['password'])
               request.session['email']=manager.email

               return Response({'message':"Manager Logged in Successfully.."})
            except Manager.DoesNotExist:
                return  Response({'message':'Invalid EmailId and password'})

        return Response(ls.errors)



class ManagerLogout(CreateAPIView):
    serializer_class = LogoutSerializer



    def post(self, request,*args, **kwargs,):
        lout=LogoutSerializer(data=request.data)
        if lout.is_valid():
            try:
                manager=Manager.objects.get(email=lout.validated_data['email'])
                if manager.email==request.session['email']:
                    del request.session['email']
                    return Response({'message': 'manager successfully Loggedout...'})
                else:
                    return Response({'message':"Manager email is not matching.."})

            except KeyError:
                return Response({'message':'Pleas do login'})
            except Manager.DoesNotExist:
                return Response({"message":"Invalid Email"})
        return Response(lout.errors)





class CreateEmployee(CreateAPIView):
    serializer_class = EmployeeSerializer

    def post(self, request, *args, **kwargs):
        es=EmployeeSerializer(data=request.data)
        if es.is_valid():
            try:
                if request.session['email']:
                    es.save()
                    return Response(es.data)
                else:
                    return Response({'message': "please do login"})
            except KeyError:
                return Response({'message':"Manager is not logged in You cannot employee"})


        else:
            return Response(es.errors)




class EmployeesList(APIView):

    def get(self,request):

        queryset =  Employee.objects.all().order_by('firstname', 'lastname')
        es = EmployeeSerializer(queryset,many=True)
        if es:
            try:
                if request.session['email']:
                    return Response(es.data)
                else:
                    return Response({'message': "please do login"})
            except KeyError:
                return Response({'message':"Manager is not logged in You cannot View employee"})


        else:
            return Response(es.errors)





class UpdateEmployee(UpdateAPIView):
    serializer_class = EmployeeSerializer
    def patch(self, request, *args, **kwargs):




        es=EmployeeSerializer(data=request.data,partial=True)
        if es.is_valid():
            try:
                if request.session['email']:
                    es.save()
                    return Response(es.data)
                else:
                    return Response({'message': "please do login"})
            except KeyError:
                return Response({'message': "Manager is not logged in You cannot employee"})


        else:
            return Response(es.errors)


# queryset = Employee.objects.all()













class EmployeeOpers(RetrieveUpdateDestroyAPIView):


    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

# Create your views here
