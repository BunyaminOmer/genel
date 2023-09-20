import requests
r = requests.get("https://www.w3schools.com")
print(f"Response [{r.status_code}]")