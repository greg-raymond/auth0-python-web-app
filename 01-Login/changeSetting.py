import json
import http.client

conn = http.client.HTTPSConnection("<domain name here>")

payload = "{\"client_id\":\"\",\"client_secret\":\"\",\"audience\":\"\",\"grant_type\":\"client_credentials\"}"

headers = { 'content-type': "application/json" }

conn.request("POST", "/oauth/token", payload, headers)

res = conn.getresponse()
data = res.read()

json = json.loads(data.decode("utf-8"));


payload = "{ \"flags\": { \"use_scope_descriptions_for_consent\": true } }"

headers = {
    'content-type': "application/json",
    'authorization': "Bearer " + json['access_token'],
    'cache-control': "no-cache"
    }

conn.request("PATCH", "/api/v2/tenants/settings", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
