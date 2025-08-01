#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import shutil

source_folder = "source_folder_path"
destination_folder = "destination_folder_path"

# Make sure destination exists
os.makedirs(destination_folder, exist_ok=True)

# Move .jpg files
for filename in os.listdir(source_folder):
    if filename.lower().endswith('.jpg'):
        full_path = os.path.join(source_folder, filename)
        shutil.move(full_path, os.path.join(destination_folder, filename))
        print(f"Moved: {filename}")

print("✅ All .jpg files moved.")


# In[ ]:


import re

input_file = "input.txt"
output_file = "emails.txt"

# Read text from file
with open(input_file, 'r') as file:
    content = file.read()

# Regex to extract emails
emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', content)

# Remove duplicates
emails = list(set(emails))

# Save to output file
with open(output_file, 'w') as file:
    for email in emails:
        file.write(email + '\n')

print(f"✅ {len(emails)} email(s) extracted and saved to {output_file}.")


# In[ ]:


import requests
import re

url = "https://example.com"  # Replace with the page you want

response = requests.get(url)

# Find title using regex
match = re.search(r'<title>(.*?)</title>', response.text, re.IGNORECASE | re.DOTALL)

if match:
    title = match.group(1).strip()
    with open("page_title.txt", 'w') as file:
        file.write(title)
    print(f"✅ Page title saved: '{title}'")
else:
    print("❌ Title not found.")

