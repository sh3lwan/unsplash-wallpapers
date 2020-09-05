import requests
import shutil
import string, random
import os
from os import path
import ctypes

# Create folder on C: If doesn't exist
current_path = 'C:\\wallpapers\\'
try:
    if not os.path.exists(current_path):
        os.makedirs(current_path)
except OSError as e:
    raise

access_token = "YOUR_ACCESS_KEY";
client_id = f"Client-ID {access_token}"

#Collectins of Wallpapers
collection_ids = [123180,782123,420,1527015,268237,235]
string_ints = [str(int) for int in collection_ids]

url = f"https://api.unsplash.com/photos/random?collections={','.join(string_ints)}"

response = requests.get(url, headers={"Accept-Version":"v1", "Authorization": client_id})

if response.status_code == 200:
    image_body = response.json()
    image_url = image_body['urls']['raw']
    file_name = image_body['id'] + '.jpg'
    full_path = current_path + file_name

    # If file exists, no need to create new image
    if path.exists(full_path):
        print('File already there')
        exit()

    # Get Image from URL
    image_response = requests.get(image_url, stream = True)

    if(image_response.status_code == 200):
        r.raw.decode_content = True
        with open(full_path,'wb') as f:
            shutil.copyfileobj(image_response.raw, f)

    if(path.exists(full_path)):
        ctypes.windll.user32.SystemParametersInfoW(20, 0,full_path, 0)
else:
    print(f'{response.status_code} {response.text}')


