import requests

from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view

# Create your views here.

@api_view(["POST"])
def transactionPost(request):
    if request.method == "POST":
        data = {}
        cr = request.data.get("cr", None)
        dr = request.data.get("dr", None)
        country_code = request.data.get("countryCode", "")
        transaction_id = request.data.get("transactionId", "")
        transaction_date = request.data.get("transactionDate", "")
        transaction_type = request.data.get("transactionType", "")

        if not cr or not dr:
            message = f"CR or DR Data Missing!"
            return JsonResponse(
                {
                        "responseObject": {
                            "code": 0,
                            'data': message
                        },
                        "statusCode": "00",
                        "successful": True,
                        "statusMessage": "Success"                        
                    }
            )
        # Source Details
        dr_amount = dr["amount"]
        dr_channel = dr["channel"]
        dr_account = dr["account"]
        dr_currency = dr["currency"]
        dr_customer_id = dr["customerId"]
        dr_customer_name = dr["customerName"]
        
        # Destionation
        cr_amount = cr["amount"]
        cr_channel = cr["channel"]
        cr_account = cr["account"]
        cr_currency = cr["currency"]
        cr_customerId = cr["customerId"]
        cr_customer_name = cr["customerName"]        

        print(" ---------------------------------------------- ")
        print(f"transaction_date -->{transaction_date}")
        print(f"transaction_id -->{transaction_id}")
        print(f"transaction_type -->{transaction_type}")
        print(f"country_code -->{country_code}")
        # Source Details
        print(f"dr -->{dr}")
        print(f"dr_customer_id -->{dr_customer_id}")
        print(f"dr_channel -->{dr_channel}")
        print(f"dr_currency -->{dr_currency}")
        print(f"dr_customer_name -->{dr_customer_name}")
        print(f"dr_amount -->{dr_amount}")
        print(f"dr_account -->{dr_account}")
        # Destionation
        print(f"cr -->{cr}")
        print(f"cr_customerId -->{cr_customerId}")
        print(f"cr_channel -->{cr_channel}")
        print(f"cr_currency -->{cr_currency}")
        print(f"cr_customer_name -->{cr_customer_name}")
        print(f"cr_amount -->{cr_amount}")
        print(f"cr_account -->{cr_account}")
        print(" ---------------------------------------------- ")

        # Sending Data to Rule Engine
        url = settings.RULE_ENGINE_URL
        headers = {"Content-Type": "application/json"}
        content = {
            cr_amount: cr_amount,
            cr_channel: cr_channel,
            cr_account: cr_account,
            cr_currency: cr_currency,
            cr_customerId: cr_customerId,
            cr_customer_name: cr_customer_name,

            dr_amount: dr_amount,
            dr_channel: dr_channel,
            dr_account: dr_account,
            dr_currency: dr_currency,
            dr_customer_id: dr_customer_id,
            dr_customer_name: dr_customer_name,

            country_code: country_code,
            transaction_id: transaction_id,
            transaction_date: transaction_date,
            transaction_type: transaction_type
        }

        try:
            response = requests.post(url, headers=headers, data=content)
            
            json_response = response.json()
            print(f"Json Response ---> {json_response}")
        except Exception as e:
            message = f"Unable to reach the Rule Engine! Error Experienced --> {e}"
            return JsonResponse(
                {
                        "responseObject": {
                            "code": 0,
                            'data': message
                        },
                        "statusCode": "00",
                        "successful": True,
                        "statusMessage": "Success"                        
                    }
            )

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