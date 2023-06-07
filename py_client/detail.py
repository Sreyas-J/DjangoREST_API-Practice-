import requests

endpoint="http://localhost:8000/api/products/10/"

get_response=requests.get(endpoint,json={"title":"abc123","content":"Hello world"})
print(get_response.json())