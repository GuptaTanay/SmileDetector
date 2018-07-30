import http.client, urllib.request
import urllib.parse, urllib.error
import base64, sys
import simplejson as json

# replace with subscription_key
# you obtained after registration
subscription_key = 'd7261136e76c48dd919d11bda993e08e'

headers = {

    # Request headers. Replace
    # the placeholder key
    # below with your
    # subscription key.
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

params = urllib.parse.urlencode({
})

# Replace the URL
# below with the
# URL of the image
# you want to analyze.
url1 = 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Girl_Portrait_Kid_Cute_Hair_Sunlight_Arab_Young.jpg/220px-Girl_Portrait_Kid_Cute_Hair_Sunlight_Arab_Young.jpg'
body = {'url': url1}
newbody = str(body)

try:
    # NOTE: You must use the same region in your REST call as you used to obtain your subscription keys.
    # For example, if you obtained your subscription keys from westcentralus, replace "westus" in the
    # URL below with "westcentralus".
    conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, newbody, headers)
    response = conn.getresponse()
    data = response.read()

    parsed = json.loads(data)
    print("Response:")
    print(json.dumps(parsed, sort_keys=True, indent=2))

    # the emotion of image
    # will the max value of
    # any emotion obtained
    # from the different
    # scores of each emotion
    val = parsed[0]["scores"]
    res = max(val, key=val.get)
    print("\nEmotion :: ", res)

    conn.close()
except Exception as e:
    print(e.args)
