import requests
import re

url = input("> Enter the website URL: ")

try:
    response = requests.get(url)
    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", response.text)
    if emails:
        print("> Found emails:")
        for email in set(emails):
            print(email)
    else:
        print("> No emails found.")
except Exception as e:
    print("> Error:", e)
