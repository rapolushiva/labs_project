

#========================CLIENT_INFO===================================

import requests

# Define the API endpoint URL
url = 'http://localhost:5000/add_client_info'

# Define the JSON data to send in the request
data = {
        "email_id": "john@example.com",
        "name": "John Doe",
        "mobile": "123-456-7890",
        "location": "New York",
        "biz_name": "Doe Enterprises",
        "est_date": "2020-01-15",
        "dob": "1980-05-20",
        "gender": "Male",
        "domain_name": "johndoe.com",
        "plan": "Premium",
        "pincode": "10001",
        "Referred_by": "jane@example.com",
        "Referal_Code": "ABCD123",
        "Referral_Self": "No",
        "Created_date": "2023-03-10",
        "Expire_date": "2024-03-10",
        "Plan_duration": "1 Year",
        "As_branch": "Branch A"
    }

# Set the headers for JSON content
headers = {'Content-Type': 'application/json'}

# Send the POST request
response = requests.post(url, json=data, headers=headers)


import requests

# Define the API endpoint URL
url = 'http://localhost:5000/add_client_info'

# Define the JSON data to send in the request
data = {

        "email_id": "jane@example.com",
        "name": "Jane Smith",
        "mobile": "987-654-3210",
        "location": "Los Angeles",
        "biz_name": "Smith Co.",
        "est_date": "2018-07-20",
        "dob": "1990-12-05",
        "gender": "Female",
        "domain_name": "janesmith.com",
        "plan": "Basic",
        "pincode": "90001",
        "Referred_by": 'shiva@gmail.com',
        "Referal_Code": 'ABCD1234',
        "Referral_Self": "Yes",
        "Created_date": "2023-02-15",
        "Expire_date": "2023-12-15",
        "Plan_duration": "100 days",
        "As_branch": "Branch B"
    }

# Set the headers for JSON content
headers = {'Content-Type': 'application/json'}

# Send the POST request
response = requests.post(url, json=data, headers=headers)

# Print the response
print(response.status_code)  # HTTP status code
print(response.json())      #

#================ADD_PLAN====================================
import requests

# Define the API endpoint URL
url = 'http://localhost:5000/add_plan'

# Define the JSON data to send in the request
data = {
        "plan_name": "Enterprise Plan",
        "plan_amount": 99.99,
        "discount": 15.0,
        "plan_duration": "1 month",
        "enable_SMS_reminder": "true",
        "enable_whatsapp_reminder": "false",
        "enable_basic_dashboard": "true",
        "enable_advanced_dashboard": "false",
        "enable_monthly_reports": "true",
        "enable_weekly_reports": "false",
        "data_download_permission": "true",
        "created_date": "2023-09-03",
        "created_by": "Admin"
    }

# Set the headers for JSON content
headers = {'Content-Type': 'application/json'}

# Send the POST request
response = requests.post(url, json=data, headers=headers)


url = 'http://localhost:5000/add_plan'

# Define the JSON data to send in the request
data = {
        "plan_name": "Premium Plan",
        "plan_amount": 49.99,
        "discount": 10.0,
        "plan_duration": "1 month",
        "enable_SMS_reminder": "true",
        "enable_whatsapp_reminder": "false",
        "enable_basic_dashboard": "true",
        "enable_advanced_dashboard": "false",
        "enable_monthly_reports": "true",
        "enable_weekly_reports": "false",
        "data_download_permission": "true",
        "created_date": "2023-08-02",
        "created_by": "Admin"
        
    }

# Set the headers for JSON content
headers = {'Content-Type': 'application/json'}

# Send the POST request
response = requests.post(url, json=data, headers=headers)


# Print the response
print(response.status_code)  # HTTP status code
print(response.json())      # Response data as JSON


url = 'http://localhost:5000/add_plan'

# Define the JSON data to send in the request
data = {
    "plan_name": "Basic Plan",
    "plan_amount": 19.99,
    "discount": 0.0,
    "plan_duration": "1 month",
    "enable_SMS_reminder": "true",
    "enable_whatsapp_reminder": "false",
    "enable_basic_dashboard": "true",
    "enable_advanced_dashboard": "false",
    "enable_monthly_reports": "true",
    "enable_weekly_reports": "false",
    "data_download_permission": "true",
    "created_date": "2023-09-15",
    "created_by": "admin@example.com"
}

# Set the headers for JSON content
headers = {'Content-Type': 'application/json'}

# Send the POST request
response = requests.post(url, json=data, headers=headers)


# Print the response
print(response.status_code)  # HTTP status code
print(response.json()) 

#======================DOMAIN_DATA================

import requests

# Define the API endpoint URL
url = 'http://localhost:5000/add_domain'

# Define the JSON data to send in the request
data = {
    "domain_name": "healthcare",
    "domain_id": 3
}

# Set the headers for JSON content
headers = {'Content-Type': 'application/json'}

# Send the POST request
response = requests.post(url, json=data, headers=headers)

import requests

# Define the API endpoint URL
url = 'http://localhost:5000/add_domain'

# Define the JSON data to send in the request
data = {
    "domain_name": "automobile",
    "domain_id": 4
}

# Set the headers for JSON content
headers = {'Content-Type': 'application/json'}

# Send the POST request
response = requests.post(url, json=data, headers=headers)

# Print the response
print(response.status_code)  # HTTP status code
print(response.json())      # Response data as JSON


#===============TENANT_DATA======================

    
import requests
import json

url = "http://localhost:5000/tenants"

payload = json.dumps({
  "tenant_mail": "ten@gmail.com",
  "tenant_mobile": "9320392092",
  "tenant_name": "Tenant ABC",
  "client_id": "branch3@example.com",
  "client_name": "Aler"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


    
import requests
import json

url = "http://localhost:5000/tenants"

payload = json.dumps({
  "tenant_mail": "ten@gmail.com",
  "tenant_mobile": "9320392092",
  "tenant_name": "Tenant ABC",
  "client_id": "branch3@example.com",
  "client_name": "Aler"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

    
import requests
import json

url = "http://localhost:5000/tenants"

payload = json.dumps({
  "tenant_mail": "ten@gmail.com",
  "tenant_mobile": "9320392092",
  "tenant_name": "Tenant ABC",
  "client_id": "branch3@example.com",
  "client_name": "Aler"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)



#==================CUSTOMER_DATA============================

import requests

# Define the API endpoint URL
url = 'http://localhost:5000/add_customer_info'

# Define the JSON data to send in the request
data = {
    "Customer_name":'customer123',
    "customer_mail": "customer@example.com",
    "customer_mobile": "123-456-7890",
    "customer_alternate_mobile": "987-654-3210",
    "customer_whatsapp_number": "789-123-4567",
    "customer_age": 30,
    "customer_gender": "Male",
    "customer_location": "New York",
    "customer_pincode": "10001",
    "client_id": "jane@example.com",
    "client_name": "Jane Smith"
    
}

# Set the headers for JSON content
headers = {'Content-Type': 'application/json'}

# Send the POST request
response = requests.post(url, json=data, headers=headers)

# Print the response
print(response.status_code)  # HTTP status code
print(response.json())      # Response content


import requests

# Define the API endpoint URL
url = 'http://localhost:5000/add_customer_info'

# Define the JSON data to send in the request
data = {
    "Customer_name":'customer555',
    "customer_mail": "anothercustomer@example.com",
    "customer_mobile": "555-555-5555",
    "customer_alternate_mobile": "444-444-4444",
    "customer_whatsapp_number": "666-666-6666",
    "customer_age": 28,
    "customer_gender": "Female",
    "customer_location": "Los Angeles",
    "customer_pincode": "90001",
    "client_id": "john@example.com",
    "client_name": "John Doe"
}

# Set the headers for JSON content
headers = {'Content-Type': 'application/json'}

# Send the POST request
response = requests.post(url, json=data, headers=headers)

# Print the response
print(response.status_code)  # HTTP status code
print(response.json())      # Response content


#==========================Tenant_service===================
import requests

# Define the API endpoint URLs for adding data
tenant_service_url = 'http://localhost:5000/add_tenant_service'
# Define the JSON data to send in the request for 'tenant_service_db'
tenant_service_data = {
    "client_email_id": "jane@example.com",  # Assuming this is the email_id from 'client_info'
    "service_name": "Service A",
    "category": "Category 1",
    "selling_price": 50.0,
    "MRP": 60.0,
    "discount": 10.0,
    "is_active": True,
    "created_by": "Admin",
    "created_at": "2023-09-29",
    "modified_by": "Admin",
    "modified_date": "2023-09-29",
    "sub_category": "Subcategory X"
}


# Set the headers for JSON content
headers = {'Content-Type': 'application/json'}

# Send the POST request to add data to 'tenant_service_db'
tenant_service_response = requests.post(tenant_service_url, json=tenant_service_data, headers=headers)

# Print the response for 'tenant_service_db'
print("Adding Tenant Service Response:")
print(tenant_service_response.status_code)  # HTTP status code
print(tenant_service_response.json())      # Response content
#===========================
import requests

# Define the API endpoint URLs for adding data
tenant_service_url = 'http://localhost:5000/add_tenant_service'
# Define the JSON data to send in the request for 'tenant_service_db'
tenant_service_data = {
    "client_email_id": "jane@example.com",  # Assuming this is the email_id from 'client_info'
    "service_name": "Blood Service",
    "category": "Category 1",
    "selling_price": 50.0,
    "MRP": 60.0,
    "discount": 10.0,
    "is_active": True,
    "created_by": "Admin",
    "created_at": "2023-09-29",
    "modified_by": "Admin",
    "modified_date": "2023-09-29",
    "sub_category": "Subcategory X"
}


# Set the headers for JSON content
headers = {'Content-Type': 'application/json'}

# Send the POST request to add data to 'tenant_service_db'
tenant_service_response = requests.post(tenant_service_url, json=tenant_service_data, headers=headers)

# Print the response for 'tenant_service_db'
print("Adding Tenant Service Response:")
print(tenant_service_response.status_code)  # HTTP status code
print(tenant_service_response.json())  

#===========tenat_service==================


tenant_service_url = 'http://localhost:5000/add_tenant_service'
# Define another JSON data to send in the request for 'tenant_service_db'
tenant_service_data_2 = {
    "client_email_id": "jane@example.com",  # Assuming this is the email_id from 'client_info'
    "service_name": "Urine Test",
    "category": "Category 3",
    "selling_price": 65.0,
    "MRP": 70.0,
    "discount": 5.0,
    "is_active": True,
    "created_by": "Admin",
    "created_at": "2023-09-30",
    "modified_by": "Admin",
    "modified_date": "2023-10-20",
    "sub_category": "Subcategory Z"
}

# Set the headers for JSON content
headers = {'Content-Type': 'application/json'}
# Send the POST request to add data to 'tenant_service_db' for the second entry
tenant_service_response_2 = requests.post(tenant_service_url, json=tenant_service_data_2, headers=headers)

# Print the response for the second entry in 'tenant_service_db'
print("\nAdding Second Tenant Service Response:")
print(tenant_service_response_2.status_code)  # HTTP status code
print(tenant_service_response_2.json())      # Response content
#===================
import requests

# Define the API endpoint URLs for adding data
tenant_service_url = 'http://localhost:5000/add_tenant_service'
# Define the JSON data to send in the request for 'tenant_service_db'
tenant_service_data = {
    "client_email_id": "jane@example.com",  # Assuming this is the email_id from 'client_info'
    "service_name": " Biopsy",
    "category": "Category 1",
    "selling_price": 50.0,
    "MRP": 60.0,
    "discount": 10.0,
    "is_active": True,
    "created_by": "Admin",
    "created_at": "2023-09-29",
    "modified_by": "Admin",
    "modified_date": "2023-09-29",
    "sub_category": "Subcategory X"
}


# Set the headers for JSON content
headers = {'Content-Type': 'application/json'}

# Send the POST request to add data to 'tenant_service_db'
tenant_service_response = requests.post(tenant_service_url, json=tenant_service_data, headers=headers)

# Print the response for 'tenant_service_db'
print("Adding Tenant Service Response:")
print(tenant_service_response.status_code)  # HTTP status code
print(tenant_service_response.json())      # Response content

#=============================

import requests

# Define the API endpoint URLs for adding data
tenant_service_url = 'http://localhost:5000/add_tenant_service'
# Define the JSON data to send in the request for 'tenant_service_db'
tenant_service_data = {
    "client_email_id": "jane@example.com",  # Assuming this is the email_id from 'client_info'
    "service_name": " HbA1c test",
    "category": "Category 1",
    "selling_price": 50.0,
    "MRP": 60.0,
    "discount": 10.0,
    "is_active": True,
    "created_by": "Admin",
    "created_at": "2023-09-29",
    "modified_by": "Admin",
    "modified_date": "2023-09-29",
    "sub_category": "Subcategory X"
}


# Set the headers for JSON content
headers = {'Content-Type': 'application/json'}

# Send the POST request to add data to 'tenant_service_db'
tenant_service_response = requests.post(tenant_service_url, json=tenant_service_data, headers=headers)

# Print the response for 'tenant_service_db'
print("Adding Tenant Service Response:")
print(tenant_service_response.status_code)  # HTTP status code
print(tenant_service_response.json())      # Response content

#============================

import requests

# Define the API endpoint URLs for adding data
tenant_service_url = 'http://localhost:5000/add_tenant_service'
# Define the JSON data to send in the request for 'tenant_service_db'
tenant_service_data = {
    "client_email_id": "jane@example.com",  # Assuming this is the email_id from 'client_info'
    "service_name": " Basic metabolic panel",
    "category": "Category 1",
    "selling_price": 50.0,
    "MRP": 60.0,
    "discount": 10.0,
    "is_active": True,
    "created_by": "Admin",
    "created_at": "2023-09-29",
    "modified_by": "Admin",
    "modified_date": "2023-09-29",
    "sub_category": "Subcategory X"
}


# Set the headers for JSON content
headers = {'Content-Type': 'application/json'}

# Send the POST request to add data to 'tenant_service_db'
tenant_service_response = requests.post(tenant_service_url, json=tenant_service_data, headers=headers)

# Print the response for 'tenant_service_db'
print("Adding Tenant Service Response:")
print(tenant_service_response.status_code)  # HTTP status code
print(tenant_service_response.json())      # Response content

#============================

import requests

# Define the API endpoint URLs for adding data
tenant_service_url = 'http://localhost:5000/add_tenant_service'
# Define the JSON data to send in the request for 'tenant_service_db'
tenant_service_data = {
    "client_email_id": "jane@example.com",  # Assuming this is the email_id from 'client_info'
    "service_name": "Blood count",
    "category": "Category 1",
    "selling_price": 40.0,
    "MRP": 50.0,
    "discount": 5.0,
    "is_active": True,
    "created_by": "Admin",
    "created_at": "2023-09-29",
    "modified_by": "Admin",
    "modified_date": "2023-09-29",
    "sub_category": "Subcategory X"
}


# Set the headers for JSON content
headers = {'Content-Type': 'application/json'}

# Send the POST request to add data to 'tenant_service_db'
tenant_service_response = requests.post(tenant_service_url, json=tenant_service_data, headers=headers)

# Print the response for 'tenant_service_db'
print("Adding Tenant Service Response:")
print(tenant_service_response.status_code)  # HTTP status code
print(tenant_service_response.json())      # Response content

#=====================
import requests

# Define the API endpoint URLs for adding data
tenant_service_url = 'http://localhost:5000/add_tenant_service'
# Define the JSON data to send in the request for 'tenant_service_db'
tenant_service_data = {
    "client_email_id": "jane@example.com",  # Assuming this is the email_id from 'client_info'
    "service_name": "Cholesterol test",
    "category": "Category 1",
    "selling_price": 70.0,
    "MRP": 80.0,
    "discount": 10.0,
    "is_active": True,
    "created_by": "Admin",
    "created_at": "2023-09-29",
    "modified_by": "Admin",
    "modified_date": "2023-09-29",
    "sub_category": "Subcategory X"
}


# Set the headers for JSON content
headers = {'Content-Type': 'application/json'}

# Send the POST request to add data to 'tenant_service_db'
tenant_service_response = requests.post(tenant_service_url, json=tenant_service_data, headers=headers)

# Print the response for 'tenant_service_db'
print("Adding Tenant Service Response:")
print(tenant_service_response.status_code)  # HTTP status code
print(tenant_service_response.json())      # Response content

#===================
import requests

# Define the API endpoint URLs for adding data
tenant_service_url = 'http://localhost:5000/add_tenant_service'
# Define the JSON data to send in the request for 'tenant_service_db'
tenant_service_data = {
    "client_email_id": "jane@example.com",  # Assuming this is the email_id from 'client_info'
    "service_name": "Liver function tests",
    "category": "Category 1",
    "selling_price": 110.0,
    "MRP": 120.0,
    "discount": 24.0,
    "is_active": True,
    "created_by": "Admin",
    "created_at": "2023-09-29",
    "modified_by": "Admin",
    "modified_date": "2023-09-29",
    "sub_category": "Subcategory X"
}


# Set the headers for JSON content
headers = {'Content-Type': 'application/json'}

# Send the POST request to add data to 'tenant_service_db'
tenant_service_response = requests.post(tenant_service_url, json=tenant_service_data, headers=headers)

# Print the response for 'tenant_service_db'
print("Adding Tenant Service Response:")
print(tenant_service_response.status_code)  # HTTP status code
print(tenant_service_response.json())      # Response content
#============================
import requests

# Define the API endpoint URLs for adding data
tenant_service_url = 'http://localhost:5000/add_tenant_service'
# Define the JSON data to send in the request for 'tenant_service_db'
tenant_service_data = {
    "client_email_id": "jane@example.com",  # Assuming this is the email_id from 'client_info'
    "service_name": "Arterial blood gas test",
    "category": "Category 2",
    "selling_price": 70.0,
    "MRP": 80.0,
    "discount": 10.0,
    "is_active": True,
    "created_by": "Admin",
    "created_at": "2023-09-29",
    "modified_by": "Admin",
    "modified_date": "2023-09-29",
    "sub_category": "Subcategory X"
}


# Set the headers for JSON content
headers = {'Content-Type': 'application/json'}

# Send the POST request to add data to 'tenant_service_db'
tenant_service_response = requests.post(tenant_service_url, json=tenant_service_data, headers=headers)

# Print the response for 'tenant_service_db'
print("Adding Tenant Service Response:")
print(tenant_service_response.status_code)  # HTTP status code
print(tenant_service_response.json())      # Response content

#=========================
import requests

# Define the API endpoint URLs for adding data
tenant_service_url = 'http://localhost:5000/add_tenant_service'
# Define the JSON data to send in the request for 'tenant_service_db'
tenant_service_data = {
    "client_email_id": "jane@example.com",  # Assuming this is the email_id from 'client_info'
    "service_name": "Hematocrit",
    "category": "Category 3",
    "selling_price": 70.0,
    "MRP": 80.0,
    "discount": 10.0,
    "is_active": True,
    "created_by": "Admin",
    "created_at": "2023-09-29",
    "modified_by": "Admin",
    "modified_date": "2023-09-29",
    "sub_category": "Subcategory X"
}


# Set the headers for JSON content
headers = {'Content-Type': 'application/json'}

# Send the POST request to add data to 'tenant_service_db'
tenant_service_response = requests.post(tenant_service_url, json=tenant_service_data, headers=headers)

# Print the response for 'tenant_service_db'
print("Adding Tenant Service Response:")
print(tenant_service_response.status_code)  # HTTP status code
print(tenant_service_response.json())      # Response content
#=======================



import requests

# Define the API endpoint URL
url = 'http://localhost:5000/add_customer_info'

# Define the JSON data to send in the request
data = {
    "Customer_name":"sai",
    "Customer_mail": "test1@example.com",
    "Customer_mobile": "9823748523",
    "Customer_alternate_mobile": "8923452374",
    "Customer_whatsapp_number": "8234235438",
    "Customer_age": 23,
    "Customer_gender": "male",
    "Customer_location": "Los Angeles",
    "Customer_pincode": "90001",
    "client_id": "john@example.com",
    "client_name": "John Doe"

}

# Set the headers for JSON content
headers = {'Content-Type': 'application/json'}

# Send the POST request
response = requests.post(url, json=data, headers=headers)

# Print the response
print(response.status_code)  # HTTP status code
print(response.json())      # Response content
# import requests

# # Define the API endpoint URLs for adding data
# tenant_service_url = 'http://localhost:5000/add_tenant_service'
# tenant_service_data_2 = {
#     "client_email_id": "jane@example.com",  # Assuming this is the email_id from 'client_info'
#     "service_name": "Test",
#     "category": "Category5",
#     "selling_price": 100.0,
#     "MRP": 100.0,
#     "discount": 10.0,
#     "is_active": True,
#     "created_by": "Admin",
#     "created_at": "2023-09-30",
#     "modified_by": "Admin",
#     "modified_date": "2023-10-20",
#     "sub_category": "Subcategory Z"
# }

# # Set the headers for JSON content
# headers = {'Content-Type': 'application/json'}
# # Send the POST request to add data to 'tenant_service_db' for the second entry
# tenant_service_response_2 = requests.post(tenant_service_url, json=tenant_service_data_2, headers=headers)

# # Print the response for the second entry in 'tenant_service_db'
# print("\nAdding Tenant Service Response:")
# print(tenant_service_response_2.status_code)  # HTTP status code
# print(tenant_service_response_2.json())  


#<=================Transaction_details=======================>

# import requests

# # Define the API endpoint URL
# url = 'http://localhost:5000/add_customer_transaction'

# # Define the JSON data to send in the request
# data = {
#     "Customer_id":'',
#     "Customer_name":"",
#     "Service_name": "Service B",
#     "Remainder_days": 30,
#     "Current_date": "2023-09-20",
#     "Current_service_remark": "Service B remark",
#     "Payment_Mode": "Card",
#     "Paid_amount": 45.50,
#     "Discount": 7.5,
#     "Location": "Los Angeles"
# }

# # Set the headers for JSON content
# headers = {'Content-Type': 'application/json'}

# # Send the POST request
# response = requests.post(url, json=data, headers=headers)

# # Print the response
# print(response.status_code)  # HTTP status code
# print(response.json())      # Response content

# #=====================

# import requests

# # Define the API endpoint URL
# url = 'http://localhost:5000/add_customer_transaction'

# # Define the JSON data to send in the request
# data = {
#     "Service_name": "Service A",
#     "Remainder_days": 15,
#     "Current_date": "2023-09-15",
#     "Current_service_remark": "Service A remark",
#     "Payment_Mode": "online",
#     "Paid_amount": 25.99,
#     "Discount": 5.0,
#     "Location": "New York"
# }

# # Set the headers for JSON content
# headers = {'Content-Type': 'application/json'}

# # Send the POST request
# response = requests.post(url, json=data, headers=headers)

# # Print the response
# print(response.status_code)  # HTTP status code
# print(response.json())      # Response content

