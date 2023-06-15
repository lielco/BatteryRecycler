import json
import requests

admin_path = 'http://127.0.0.1:8000/admin/rules'
customer_id = "111111"
pickup_path = f'http://127.0.0.1:8000/api/customer/{customer_id}/pickup'

print('### HAPPY FLOW ###')
print('### Put new rule file ###')
print(f'PUT {admin_path}')
with open('demo/rules.json', 'rb') as file:
    files = {'rules_file': file}
    put_rules_response = requests.put(admin_path, files=files)
    print(f'{put_rules_response.status_code}: {put_rules_response.content}')

print()
print('### Post pickup request ###')
print(f'POST {pickup_path}')
multipart_form_data = {
    'battery_capacity': (None, 15000),
    'battery_age': (None, 3),
    'battery_type': (None, 'batteryA'),
    'amount': (None, 2),
    'us_state': (None, 'NY')
}
print(f'Request data: {multipart_form_data}')

pickup_response = requests.post(pickup_path, files=multipart_form_data)
pickup_json = pickup_response.json()
print(f'{pickup_response.status_code}: {pickup_json}')
pickup_id = pickup_json.get('pickup_id')

print()
print('### Get pickup request ###')
print(f'GET {pickup_path}/{pickup_id}')
pickup_info_response = requests.get(f'{pickup_path}/{pickup_id}')
print(f'{pickup_info_response.status_code}: {pickup_info_response.json()}')

print()
print('### Approve pickup request ###')
print(f'PATCH {pickup_path}/{pickup_id}/approval')
data = {"status": "CONFIRMED"}
print(f'Request data: {data}')
approve_response = requests.patch(f'{pickup_path}/{pickup_id}/approval', data=json.dumps(data))
print(f'{approve_response.status_code}: {approve_response.json()}')

print('### END HAPPY FLOW ###')
print()
print('### CAN\'T CALCULATE ###')

print('### Post pickup request ###')
print(f'POST {pickup_path}')
multipart_form_data = {
    'battery_capacity': (None, 15000),
    'battery_age': (None, 3),
    'battery_type': (None, 'IDontExist'),
    'amount': (None, 2),
    'us_state': (None, 'NY')
}
print(f'Request data: {multipart_form_data}')

pickup_response = requests.post(pickup_path, files=multipart_form_data)
pickup_json = pickup_response.json()
print(f'{pickup_response.status_code}: {pickup_json}')
pickup_id = pickup_json.get('pickup_id')

print('### END CAN\'T CALCULATE ###')
print()
print('### UNSUPPORTED INPUTS ###')
print('### Post pickup request ###')
print(f'POST {pickup_path}')
multipart_form_data = {
    'battery_capacity': (None, -15000),
    'battery_age': (None, 3),
    'battery_type': (None, 'batteryA'),
    'amount': (None, 2),
    'us_state': (None, 'NY')
}
print(f'Request data: {multipart_form_data}')

pickup_response = requests.post(pickup_path, files=multipart_form_data)
pickup_json = pickup_response.json()
print(f'{pickup_response.status_code}: {pickup_json}')
pickup_id = pickup_json.get('pickup_id')

print('### END UNSUPPORTED INPUTS ###')
