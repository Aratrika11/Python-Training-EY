from django.http import JsonResponse

# Create your views here.
def hello(request):
    return JsonResponse({"message":"Django API is working"})
def welcome(request):
    return JsonResponse({"msg":"Welcome to Django API"})
def status(request):
    return JsonResponse({"status":"running","framework":"Django"})