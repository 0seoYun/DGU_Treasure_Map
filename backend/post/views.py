from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import *
from .serializers import FacilitySerializer,PlaceSerializer,CategorySerializer
# Create your views here.

@api_view(['GET'])
def get_place(request, id):
    place_id = Place.objects.get(id=id)
    facilities = Facility.objects.filter(place=place_id)
    send_facility = []
    
    for i in facilities:
        place_name = place_id.name
        category_name = i.category.name

        # # facility_set = {
        # #     "name":i.name,
        # #     "category":category_name,
        # #     "id":i.id,
        # #     "time":,
        # #     "img":,
        # #     "phone":,
        # #     "use":,
        # #     "where":place_name,
        # #     "floor":
        # # }
        # send_facility.append(facility_set)

    return Response(data=send_facility)

@api_view(['GET'])
def get_category(request, id):
    place_id = Place.objects.get(id=id)
    category_id = Category.objects.get(id=id)
    facilities = Facility.objects.filter(category=category_id)

    send_place = []
    for i in facilities:
        place_name = i.place.name
        if place_name not in send_place:
            send_place.append(place_name)

    send_facility = []
    
    for i in facilities:
        place_name = place_id.name
        category_name = i.category.name

        # # facility_set = {
        # #     "name":i.name,
        # #     "category":category_name,
        # #     "id":i.id,
        # #     "time":,
        # #     "img":,
        # #     "phone":,
        # #     "use":,
        # #     "where":place_name,
        # #     "floor":
        # # }
        # send_facility.append(facility_set)

    return Response(data=send_facility)