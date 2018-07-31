import requests
import pandas as pd
subscription_key = 'Enter you key here'
assert subscription_key
emotion_recognition_url = "https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize"
headers  = {'Ocp-Apim-Subscription-Key': subscription_key, "Content-Type": "application/octet-stream" }
image_path = "Enter your file location here"
image_data = open(image_path, "rb").read()
response = requests.post(emotion_recognition_url, headers=headers, data=image_data)
response.raise_for_status()
analysis = response.json()
#print(analysis)
df=pd.DataFrame(columns=[''])
sum=0
count=0
for row in analysis:
    sum+=row['scores']['happiness']
    count+=1
avg_happiness=(sum)/count
#Location of file.txt
f=open("C:/wamp64/www/Smile/file.txt","w")
#Location of file1.txt
f1=open("C:/wamp64/www/Smile/file1.txt","w")
f.write(str(avg_happiness))
f1.write(str(count))
print("done")

