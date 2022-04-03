
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from router_api.models import Router
import re
from rest_framework.permissions import IsAuthenticated
from router_api.serializers import RouterSerializer, CreateRouterSerializer, UpdateRouterSerializer

# Create your views here.
def ip_address_validator(ip_val):
    """Function to check if given IP address(IPv4) is valid or not.
        Args: ip_val -> string
        Returns: bool -> True if ip_val is valid else False"""
    regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

    if re.search(regex,ip_val):
        return True
    else:
        return False


class Router_View(APIView):
    post_serializer = CreateRouterSerializer
    get_serializer = RouterSerializer
    patch_serializer = UpdateRouterSerializer

    permission_classes = (IsAuthenticated,)

    def get(self,request,format=None):
        """Get Endpoint to retreive list of all router objects or to filtered 
        objects based on loopback IP range given in the GET request/"""
        
        #accessing range from GET request.
        loopback_start = request.GET.get('loopback_start')
        loopback_end = request.GET.get('loopback_end')

        if loopback_start == None and loopback_end == None:
            
            router_query = Router.objects.all()

        else:
            #validating if given ranges are of IPV4 type.
            if ip_address_validator(loopback_start) or ip_address_validator(loopback_end):
                return Response({'Bad Request':'Invalid IP address found'},status=status.HTTP_400_BAD_REQUEST)

            router_query = Router.objects.filter(loopback__gte=loopback_start).filter(loopback__lte=loopback_end)

        #serializing the router queryset to return as a json object
        router_query = self.get_serializer(router_query,many=True).data

        return Response(router_query,status=status.HTTP_200_OK)

    

    def post(self,request,format=None):
        
        """Post endpoint to create new router object."""
        #validating the data received in post request body.
        serializer = self.post_serializer(data=request.data) 
        
        if serializer.is_valid():
            sapid = serializer.data.get('sapid')
            hostname = serializer.data.get("hostname")
            loopback = serializer.data.get("loopback")
            macaddress = serializer.data.get("macaddress")

            
            #create router with recieved elements.
            router = Router(sapid=sapid,hostname=hostname, loopback=loopback, macaddress=macaddress)
            router.save()

            return Response(RouterSerializer(router).data,status=status.HTTP_200_OK)
        
        else:
            return Response({'Bad Request':f'Invalid Data...{serializer.errors}'},status=status.HTTP_400_BAD_REQUEST)


    def patch(self,request,format=None):

        """PATCH endpoint to update (partial) of a given router using Unique Loopback IP."""

        try:
            loopback = request.data.get('loopback')  #checking if loopback exists in request body.
        except KeyError:
            return Response({'Bad Request':'loopback IP not found'},status=status.HTTP_400_BAD_REQUEST)
        
        router_queryset = Router.objects.filter(loopback=loopback)
            
        if not router_queryset.exists():
            return Response({'Bad Request':"Invalid loopback IP, no such router exists"},status=status.HTTP_404_NOT_FOUND)
        else:

            router = router_queryset[0]
            serializer = self.patch_serializer(router,data=request.data,partial=True)  #validating the request body as per router object.

            if serializer.is_valid():
                # if request is validated, proceed ahead.
                serializer = serializer.data
                update_fields = []
                router = router_queryset[0]
                request_data = request.data
                #accessing all the field names of router obejct.
                for field in router._meta.get_fields():
                    field = field.name
                    if field in request_data:
                        # if the filed exits in request body, update it else pass.
                        
                        setattr(router,field,request_data[field]) #router.fields = serializer[field]
                        
                        update_fields.append(field)
            
                
                router.save(update_fields=update_fields)
            
                return Response(RouterSerializer(router).data, status=status.HTTP_200_OK)    

            else:
            
                return Response({"bad request":f"Invalid Data.. {serializer.errors}"},status=status.HTTP_400_BAD_REQUEST)















