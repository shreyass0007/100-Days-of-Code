#HTTP REQUESTS
#requests.get()
#requests.put()
#request.post()
#request.delete()
import requests
from datetime import datetime

USERNAME="your user name"
TOKEN="add_YOUR token"

PIXELA_END_POINT="https://pixe.la/v1/users"
GRAPH_ID="graph1"
user_params={
    "token":"abcdefghijklmnop",
    "username":"shresh",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"

}
graph_endpoint=f"{PIXELA_END_POINT}/{USERNAME}/graphs"
graph_config={
    "id":"graph1",
    "name":"Reading Graph",
    "Unit":"pages",
    "type":"float",
    "color":"sora"

}
headers={
    "X-USER-TOKEN":TOKEN

}

# response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

PIXEL_CREATION_ENDPOINT=f"{PIXELA_END_POINT}/{USERNAME}/graphs/{GRAPH_ID}"
today=datetime.now()
print(today.strftime("%Y%m%d"))
pixel_data={
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How many pages did you read today:"),


}


response=requests.post(url=PIXEL_CREATION_ENDPOINT,json=pixel_data,headers=headers)
print(response.text)

UPDATE_END_POINT=f"{PIXELA_END_POINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"
update_data={
    "quantity":"1.0"
}

# response=requests.put(url=UPDATE_END_POINT,json=update_data,headers=headers)
# print(response.text)

DELETE_END_POINT=f"{PIXELA_END_POINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"
# response=requests.delete(url=DELETE_END_POINT,headers=headers)
# print(response.text)
