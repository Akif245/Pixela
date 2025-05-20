import requests
from datetime import datetime 

pixela="https://pixe.la/v1/users"
username="mdabdulakif"
token="asdfghjklasdfghjkl"
# valuetopraphendpnt="https://pixe.la/v1/users/a-know/graphs/test-graph"
graph_endpnt_value_insert=f"{pixela}/{username}/graphs/graph1"
graph_endpoint=f"{pixela}/{username}/graphs"



user_para={
    "token":token,
    "username":username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response=requests.post(url=pixela,json=user_para)
# print(response.text)



graph_para={
    "id":"graph1",
    "name":"Cycling graph",
    "unit":"km",
    "type":"float",
    "color":"ajisai"
    }
header={
    "X-USER-TOKEN":token

}
# response=requests.post(url=graph_endpoint,json=graph_para,headers=header)
# print(response.text)


today=datetime(year=2025,month=5,day=19)
# print(today.strftime("%Y%m%d"))

day_start="20250517"
value_para={
    "date":today.strftime("%Y%m%d"),
    "quantity":"40"


}

response=requests.post(url=graph_endpnt_value_insert,json=value_para,headers=header)
print(response.text)


