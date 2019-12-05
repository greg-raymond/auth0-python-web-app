import json
import http.client

conn = http.client.HTTPSConnection("dev-col8i0t4.auth0.com")

payload = "{\"client_id\":\"C4eZDizZRG3jhbf1Rn3H6KKM2aOIkJCZ\",\"client_secret\":\"_yzsGra-00IcfFPLyEGGVNRuRiGEUakBjQLmk83hVGQClE-GTqEeltDQWumHmctx\",\"audience\":\"https://dev-col8i0t4.auth0.com/api/v2/\",\"grant_type\":\"client_credentials\"}"

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

conn.request("GET", "/api/v2/resource-servers", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
