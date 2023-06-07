import requests

endpoint="http://localhost:8000/api/products/"

data={
    "title":"This is field done",
    "price":183
}
get_response=requests.post(endpoint,json=data)
print(get_response.json())