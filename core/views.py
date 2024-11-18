import requests
from datetime import datetime

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
            "cr_amount": cr_amount,
            "cr_channel": cr_channel,
            "cr_account": cr_account,
            "cr_currency": cr_currency,
            "cr_customerId": cr_customerId,
            "cr_customer_name": cr_customer_name,

            "dr_amount": dr_amount,
            "dr_channel": dr_channel,
            "dr_account": dr_account,
            "dr_currency": dr_currency,
            "dr_customer_id": dr_customer_id,
            "dr_customer_name": dr_customer_name,

            "country_code": country_code,
            "transaction_id": transaction_id,
            "transaction_date": transaction_date,
            "transaction_type": transaction_type
        }

        try:
            response = requests.post(url, headers=headers, json=content)
            
            json_response = response.json()
            print(f"Json Response ---> {json_response}")
            data = {
                "cr": request.data.get("cr", None),
                "dr": request.data.get("dr", None),
                "country_code": request.data.get("countryCode", ""),
                "transaction_id": request.data.get("transactionId", ""),
                "transaction_date": request.data.get("transactionDate", ""),
                "transaction_type": request.data.get("transactionType", ""),
                "score": json_response["score"],                
            }
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
                        'message': message,
                        'data': data,
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

@api_view(["POST"])
def transactionPost_v2(request):
    if request.method == "POST":
        start_time = datetime.now()

        data = {}
        cr = request.data.get("cr", None)
        dr = request.data.get("dr", None)
        deviceDetails = request.data.get("deviceDetails", None)

        bankId = request.data.get("bankId", "")
        requestId = request.data.get("requestId", "")
        customerId = request.data.get("customerId", "")
        sourceChannel = request.data.get("sourceChannel", "")
        transactionTime = request.data.get("transactionTime", "")
        transactionType = request.data.get("transactionType", "")

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
        dr_tran_id = dr["tranId"]
        dr_channel = dr["channel"]
        dr_account = dr["account"]
        dr_currency = dr["currency"]        
        dr_customer_name = dr["customerName"]
        dr_store_of_value = dr["storeOfValue"]
        dr_transaction_date = dr["transactionDate"]
        dr_transaction_type = dr["transactionType"]

        # Destionation Details
        cr_amount = cr["amount"]
        cr_tran_id = cr["tranId"]
        cr_channel = cr["channel"]
        cr_account = cr["account"]
        cr_currency = cr["currency"]        
        cr_customer_name = cr["customerName"]
        cr_store_of_value = cr["storeOfValue"]
        cr_transaction_date = cr["transactionDate"]
        cr_transaction_type = cr["transactionType"]

        # Device Details
        ip = deviceDetails["ip"]
        country = deviceDetails["country"]

        # 

        print(f"================================================================")
        print()
        print("--------------------- Data ---------------------")
        print(f"Bank ID --> {bankId}")
        print(f"Request ID --> {requestId}")
        print(f"Customer ID --> {customerId}")
        print(f"Source Channel --> {sourceChannel}")
        print(f"Transaction Time --> {transactionTime}")
        print(f"Transaction Type --> {transactionType}")
        print(" ---------------------------------------------- ")
        print()
        print("--------------------- Debit ---------------------")
        print(f"Amount --> {dr_amount}")
        print(f"Tran ID --> {dr_tran_id}")
        print(f"Channel --> {dr_channel}")
        print(f"Account --> {dr_account}")
        print(f"Currency --> {dr_currency}")
        print(f"Customer Name --> {dr_customer_name}")
        print(f"Store Of Value --> {dr_store_of_value}")
        print(f"Transaction Date --> {dr_transaction_date}")
        print(f"Transaction Type --> {dr_transaction_type}")
        print(" ---------------------------------------------- ")
        print()
        print("--------------------- Crebit ---------------------")
        print(f"Amount --> {cr_amount}")
        print(f"Tran ID --> {cr_tran_id}")
        print(f"Channel --> {cr_channel}")
        print(f"Account --> {cr_account}")
        print(f"Currency --> {cr_currency}")
        print(f"Customer Name --> {cr_customer_name}")
        print(f"Store Of Value --> {cr_store_of_value}")
        print(f"Transaction Date --> {cr_transaction_date}")
        print(f"Transaction Type --> {cr_transaction_type}")
        print(" ---------------------------------------------- ")
        print()
        print("--------------------- Device Details ---------------------")
        print(f"IP --> {ip}")
        print(f"Country --> {country}")
        print(" ---------------------------------------------- ")
        print()
        print(f"================================================================")
        
        content = {
            "bankId": bankId,
            "requestId": requestId,
            "customerId": customerId,
            "sourceChannel": sourceChannel,
            "transactionTime": transactionTime,
            "transactionType": transactionType,

            "cr_amount": cr_amount,
            "cr_tran_id": cr_tran_id,
            "cr_channel": cr_channel,
            "cr_account": cr_account,
            "cr_currency": cr_currency,
            "cr_customer_name": cr_customer_name,
            "cr_store_of_value": cr_store_of_value,
            "cr_transaction_date": cr_transaction_date,
            "cr_transaction_type": cr_transaction_type,

            "dr_amount": dr_amount,
            "dr_tran_id": dr_tran_id,
            "dr_channel": dr_channel,
            "dr_account": dr_account,
            "dr_currency": dr_currency,
            "dr_customer_name": dr_customer_name,
            "dr_store_of_value": dr_store_of_value,
            "dr_transaction_date": dr_transaction_date,
            "dr_transaction_type": dr_transaction_type,

            "ip": ip,
            "country": country,
        }

        try:
            # Sending Data to Rule Engine
            url = settings.RULE_ENGINE_V2_URL
            headers = {"Content-Type": "application/json"}
            response = requests.post(url, headers=headers, json=content)
            
            json_response = response.json()
            print(f"Json Response ---> {json_response}")
            data = {
                "cr": request.data.get("cr", None),
                "dr": request.data.get("dr", None),
                "country_code": request.data.get("countryCode", ""),
                "transaction_id": request.data.get("transactionId", ""),
                "transaction_date": request.data.get("transactionDate", ""),
                "transaction_type": request.data.get("transactionType", ""),
                "score": json_response["score"],
                "remarks": json_response["remarks"]
            }

            print(f"Data ==> {data}")

            # Save Request Payload in request table  
            print(f"======== Getting Request JSON ===========")
            print(f"CR_ACCOUNT ==> {cr_account}")
            print(f"DR_ACCOUNT ==> {dr_account}") 
            print(f"REQUEST PAYLOAD ==> {content}")  
            print(f"SCORE ==> {json_response['score']}")          
            print(f"TRANSCATION TIME ==> {transactionTime}")  
            print(f"DECISION ==> {json_response['remarks']}")  
            print(f"NAME SPACE ==> {json_response['name_space']}")  
            print(f"RESPONSE STATUS ==> {json_response['status']}")  
            print(f"RESPONSE MESSAGE ==> {json_response['message']}")  
            print(f"RESPONSE PAYLOAD ==> {json_response}")  
            
            request_json = {                
                "cr_account": cr_account,
                "dr_account": dr_account,
                "request_payload": content,
                "score": json_response["score"],
                "transaction_time": transactionTime,
                "decision": json_response["remarks"],
                "name_space": json_response["name_space"],
                "response_status": json_response["status"],
                "response_message": json_response["message"],
                "response_payload": json_response,                  
            }

            print(f"Request JSON ===> {request_json}")
            print(f"Sending data to save request function!")
            save_data = save_request_data(request_json)

            # Save data in table to be viewed by Analysts in transaction table

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
                        'message': message,
                        'data': data,
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


def save_request_data(request_json):
    print(f"Type of JSON -->{type(request_json)}")
    try:
        url = settings.SAVE_REQUEST_URL
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, headers=headers, json=request_json)
    except Exception as e:
        return f"Error on saving Request Data --> {str(e)}"
    
    return "SUCCESS!"