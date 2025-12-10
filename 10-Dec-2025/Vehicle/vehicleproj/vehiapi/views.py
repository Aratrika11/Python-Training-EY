from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Vehicle_Manufacture
import json

@csrf_exempt
def vehicles(request):

    # GET ALL EMPLOYEES
    if request.method == "GET":
        data = list(Vehicle_Manufacture.objects.values())
        return JsonResponse(data, safe=False)

    # CREATE EMPLOYEE
    if request.method == "POST":
        body = json.loads(request.body.decode('utf-8'))
        Vehicle_Manufacture.objects.create(
            number_plate=body["number_plate"],
            vehicle_type=body["vehicle_type"],
            manufacturer=body["manufacturer"],
            year=body["year"]
        )
        return JsonResponse({"message": "POST EXECUTED"})

    # UPDATE EMPLOYEE (expect id in JSON)
    if request.method == "PUT":
        body = json.loads(request.body.decode('utf-8'))
        v = Vehicle_Manufacture.objects.get(id=body["id"])
        v.number_plate = body["number_plate"]
        v.vehicle_type = body["vehicle_type"]
        v.manufacturer = body["manufacturer"]
        v.year = body["year"]
        v.save()
        return JsonResponse({"message": "PUT EXECUTED"})

    # DELETE EMPLOYEE (expect id in JSON)
    if request.method == "DELETE":
        body = json.loads(request.body.decode('utf-8'))
        v = Vehicle_Manufacture.objects.get(id=body["id"])
        v.delete()
        return JsonResponse({"message": "DELETE EXECUTED"})
