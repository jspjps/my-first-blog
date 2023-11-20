import requests    
import json      

title = input("Enter word to search: ") 
print("Word: ", title)
 
#stores the json formatted output to a variable
url = 'https://glosbe.com/gapi/translate?' \
         'from=en&dest=de&format=json&phrase=' + title
 
#json representation of url is stored in variable result
response = requests.get(url)
if response.ok:
       try:
           result = response.json()
       except json.JSONDecodeError as e:
           print("Error occurred:", str(e)) 
#get the first text in "meaning" in "tuc" from result
try:
    print("Meaning: ", result["tuc"][0]["meanings"][0]["text"])
except Exception as e:
    print("Error!")