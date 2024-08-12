from django.shortcuts import render
from rest_framework.views import APIView
from services.models import MyService
from services.serializers import MyDetailsSerialzer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class ServiceApiView(APIView):
    def get(self, request, slug = None):
        try:
            # Get One Service
            if slug is not None:
                try:
                    service = MyService.objects.get(slug = slug)
                    service_serializer = MyDetailsSerialzer(service)
                    return Response(service_serializer.data, status=status.HTTP_200_OK)
                except Exception as e:
                    return Response({"error" : "Service Not Found"}, status=status.HTTP_404_NOT_FOUND)

            # Get All Services
            service = MyService.objects.filter(active = True)
            service_serializer = MyDetailsSerialzer(service, many = True)
            return Response({
                "service" : service_serializer.data,
                "length" : len(service)
                },
            status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"error" : "Internal Server Error"})
        
    def post(self, request, id = None):
        try:
            if id is not None:
                return Response({ "error" : "Method Not Allowed" })
            else:
                service_serialzer = MyDetailsSerialzer(data=request.data)
                if service_serialzer.is_valid():
                    service_serialzer.save()
                    return Response({ "message" : "Service Added Successfully" }, status=status.HTTP_200_OK)
                else:
                    return Response(service_serialzer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({"error" : "Internal Server Error"})
        
    def put(self, request, slug = None):
        if slug is not None:
            service = MyService.objects.get(slug = slug)
            service_serializer = MyDetailsSerialzer(service, data = request.data, partial = True)
            if service_serializer.is_valid():
                service_serializer.save()
                return Response({"message" : "Updated Successfully"}, status=status.HTTP_200_OK)
            else:
                return Response(service_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({ "error" : "Method Not Allowed" })
