import json
from django.http import  JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import status
from ticket.utils import generateId, generateTicket, getPaginatedData
from ticket.serializers import TicketSerializer
from ticket.models import Ticket

class GenerateTicket(APIView):
    serializer_class = TicketSerializer

    def get(self, request):
        ip = request.GET
        #validating data
        if ip.get("set_id") is None and ip.get("room_id") is None:
            output = {
                "success": False,
                "status":400,
                "message": "set_id or room_id is missing in query"
            }
            return JsonResponse(output, status = status.HTTP_400_BAD_REQUEST)
        
        #Getting data from set_id
        if ip.get("set_id") is not None:
            data = Ticket.objects.filter(set_id=ip.get("set_id")).values("id", "ticket")
            ticket = {}
            if ip.get("page") is not None:
                data = getPaginatedData(data, int(ip.get("page")))
           
            for element in data:
                ticket[str(element["id"])] = json.loads(element["ticket"])

        #Getting data from room_id
        else:
            data = Ticket.objects.filter(room_id=ip.get("room_id")).values("id", "ticket", "set_id")
            ticket = {}
            
            if ip.get("page") is not None:
                data = getPaginatedData(data, int(ip.get("page")))

            for element in data:
                ticket[str(element["id"])] = json.loads(element["ticket"])
                    
       
            
        output = {
            "success": True,
            "status":200,
            "message": "Successful GET request",
            "tickets": ticket,
            "total_tickets": len(data)
        }
        
        return JsonResponse(output, status = status.HTTP_200_OK)
    
    def post(self, request):
        ip = request.data.copy()

        if ip.get("no_of_set") is None:
            output = {
                "success": False,
                "status":400,
                "message": "no_of_set missing in query"
            }
            return JsonResponse(output, status = status.HTTP_400_BAD_REQUEST)
        
        #generating room id in which all sets will be there
        room_id = generateId()
        set_ids = []

        #generating number of sets tickets
        for _ in range(0, int(ip["no_of_set"])):
            ticket = []
            #generate set id for each set
            set_id = generateId()
            set_ids.append(set_id)
            #generating 6 tickets for each set
            for _ in range(0,6):
                ticket = generateTicket()
                data = {
                    "room_id" : str(room_id),
                    "set_id": str(set_id),
                    "ticket": json.dumps(ticket)
                }

                #saving the data
                serializer = TicketSerializer(data=data)
                serializer.is_valid(raise_exception=True)
                serializer.save()


        output = {
            "success": True,
            "status": 201,
            "message": "Successful POST request",
            "room_id": room_id,
            "set_id": set_ids
        }
        return JsonResponse(output, status = status.HTTP_201_CREATED)

