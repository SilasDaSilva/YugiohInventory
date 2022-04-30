from distutils.file_util import write_file
import requests
import json
import pprint
import csv
import os.path


# Access API from https://db.ygoprodeck.com
response_API = requests.get('https://db.ygoprodeck.com/api/v7/cardinfo.php')

# Save data as Text and load into JSON
data_access = response_API.text
data_text= json.loads(data_access)
data= data_text['data']
inventory=[[],[],[]]

# Check if database.csv already exists
file_exists = os.path.exists('database.csv')
if file_exists == False:
       
   # Access Card ID and Name and Save into Array
   
   for id in data:
       card=[id['id'],id['name'],'not in Inventory']
       inventory.append(card)

   # Write database in CSV file
   with open('database.csv', 'w', newline='') as file:
      mywriter = csv.writer(file, delimiter=',')
      mywriter.writerows(inventory)

   print('db did not exist')

else:
   with open("database.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader: # each row is a list
        inventory.append(row)

   print('db did exist') 
   

#print(len(inventory))
#pprint.pprint(inventory)
#pprint.pprint(data)
#print(f"{id}{name}")


