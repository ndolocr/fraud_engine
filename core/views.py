from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view

# Create your views here.

api_view(["POST"])
def getTransaction(request):
    if request.method == "POST":
        
        message = f"SUCCESS!"
        return JsonResponse(
            {
                    "responseObject": {
                        "code": 1,
                        'data': message
                    },
                    "statusCode": "00",
                    "successful": True,
                    "statusMessage": "Success"                        
                }
        )
    else:
        message = f"Wrong request type. This is a 'POST' Request! "
        return JsonResponse(
            {
                "responseObject": {
                    "code": -1,
                    'data': message
                },
                "statusCode": "99",
                "successful": False,
                "statusMessage": "Fail"                        
            }
        )