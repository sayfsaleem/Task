import requests

# Replace this with your actual access token
access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk0Njc2NjQ4LCJpYXQiOjE2OTQ2NzMwNDgsImp0aSI6IjlkMmNjYTdlMWU4YjRhOGI5YzFmN2Q0YWM3ODNmYmE3IiwidXNlcl9pZCI6MTB9.DQTkd0xsOZcmZD3DPTnqw_Zmv_CKqUqFZlLWUe1ZB1Y"

headers = {
    'Authorization': f'Bearer {access_token}',  # Include "Bearer" prefix
}

response = requests.get('http://127.0.0.1:8000/profile/10/', headers=headers)

print(response.text)
