import docx2txt
from pdfminer.high_level import extract_text
import requests

file_path = input("Enter the File Path: ")

def extract_file_extension(file_path):
    file_name_split = file_path.split(".",1)
    print(file_name_split)
    if len(file_name_split) == 2:
        file_extension = file_name_split[1]
        return file_extension
    else:
        return None
    
file_extension_extract = extract_file_extension(file_path)
print(file_extension_extract)

# Extracting the Text from the PDF Or Docx:

def extract_text_from_document(file_extension_extract):
    print(file_extension_extract)
    if file_extension_extract == 'docx':
        text = docx2txt.process(file_path)
        return text
    elif file_extension_extract == 'pdf':
        text = extract_text(file_path)
        return text
    else:
        return None
    
text = extract_text_from_document(file_extension_extract)
print(text)

api_token="your_huggingface_api_token"
api_url = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"

headers = {"Authorization": f"Bearer {api_token}", "Content-Type": "application/json"}

prompt = f"""
Text Extracted: {text}

Extract the Name, Email Address, Phone Number, Companies Worked, Educational Institutions and Total Years of Work Experience from the above text extracted. Give it in Json Format strictly. For the Educational Institutions and Comapnies Worked give the names alone strictly. Dont change the order strictly and dont assign anything other than this compulsorily. Dont assign the city name along with Educational Institutions name strictly. The final data should follow the following order strictly. The final order is Name, Email Address, Phone Number, Companies Worked, Educational Institutions and Total Years of Work Experience. Give all the Educational Institutions strictly without fail. Dont assign anyother unrelated details in the final data Educational Institutions strictly. I strictly needed the final data in the key value pair. Follow all the commands in the prompt strictly. Mention the type of the data in the final data strictly for all the iterations without fail such as ```json, ```, etc.."""

data = {
    "inputs": prompt,
    "parameters":{
        "max_new_tokens": 2500,
        "do_sample": False,
        "temperature": 0.5,
        "top_k": 50,
        "top_p": 0.95,
    }
}

response = requests.post(api_url, headers=headers, json=data)
result = response.json()
data = result[0]['generated_text']
print(data)

with open('json_huggingface1.txt','w', encoding='UTF-8') as filedata:
    filedata.write(data)