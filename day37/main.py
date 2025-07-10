#HTTP REQUESTS
#requests.get()
#requests.put()
#request.post()
#request.delete()
import requests
PIXELA_END_POINT="https://pixe.la/v1/users"
user_params={
    "token":"abcdefghijklmnop",
    "username":"shresh07",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"

}
response=requests.post(url=PIXELA_END_POINT,json=user_params)
print(response.text)