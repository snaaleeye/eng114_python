import requests
import json

#post_codes_req = requests.get("https://api.postcodes.io/postcodes/nw104ls")
#print(post_codes_req.status_code) # gives us only status code
#print(post_codes_req.headers)
#print(post_codes_req.content) #prints all the content
#print((type(post_codes_req.content)) #bytes
# print(type(post_codes_req.json())) #pass through json turns to dict

#r = requests.get("https://api.postcodes.io/postcodes/nw104ls")

# print(r, type(r))

#if r.status_code == 200:
#    content = r.content
#    print(content)
#    content_json = r.json()
#    print(content_json, type(content_json))

#print eastings northings

# r = requests.get("https://api.postcodes.io/postcodes/nw104ls")
# if r.status_code == 200:
#     content = r.content
#     content_json = r.json()
#     print(content_json)
#     print(content_json['result']["eastings"])
#     print(content_json['result']["northings"])

headers = {"Content-Type": "application/json"}
data = json.dumps({"postcodes": ["OX49 5NU", "N32 0JG","NE30 1DP"]})

r = requests.post(
    url="https://api.postcodes.io/postcodes",
    headers=headers,
    data=data
)

# print(r.json())

results = r.json()['result']

print(results)
for i in results:
    print(i)
    postcodes = i['query']
    parliamentary_constituency = i['result']['parliamentary constituency']
    print(f"{postcodes} - parliamentary constituency: {parliamentary_constituency}")

# print(r.json(['result']["postcodes"]))
# print(r.json(['result']["parliamentary constituency"]))

# For each postcode print POSTCODE: region, parliamentary constituency

