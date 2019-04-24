from sys import argv
from base64 import b64encode
from json import dumps

ENCODING = 'utf-8'    
SCRIPT_NAME, IMAGE_NAME, JSON_NAME = argv    

with open(IMAGE_NAME, 'rb') as jpg_file:
	byte_content = jpg_file.read()

base64_bytes = b64encode(byte_content)

base64_string = base64_bytes.decode(ENCODING)

raw_data = {}
raw_data["name"] = IMAGE_NAME
raw_data["image_base64_string"] = base64_string

json_data = dumps(raw_data, indent=2)
with open(JSON_NAME, 'w') as json_file:
	json_file.write(json_data)
