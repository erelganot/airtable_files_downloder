import os
import requests
import string  # Import the string module

# Your Airtable API key and base ID
API_KEY = 'your_api_key'
BASE_ID = 'your_base_id'
TABLE_NAME = 'your_table_name'

# The list of attachment fields in your table
ATTACHMENT_FIELDS = [
    'Attachment 1', 'Attachment 2', 'Attachment 3', 'Attachment 4', 'Attachment 5',
    'Attachment 6', 'Attachment 7', 'Attachment 8', 'Attachment 9', 'Attachment 10',
    'Attachment 11', 'Attachment 12', 'Attachment 13', 'Attachment 14'
]

# The field name that you want to use for folder naming
FOLDER_NAME_FIELD = 'Name'

# The root directory to save downloaded files
DOWNLOAD_ROOT_DIR = './v5files'
os.makedirs(DOWNLOAD_ROOT_DIR, exist_ok=True)

# Airtable API endpoint
AIRTABLE_ENDPOINT = f'https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}'

# Headers to authenticate with the Airtable API
headers = {
    'Authorization': f'Bearer {API_KEY}'
}

def sanitize_filename(filename):
    # Remove any characters not allowed in Windows or Unix file systems
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    cleaned_filename = ''.join(c for c in filename if c in valid_chars)
    return cleaned_filename or 'unknown'  # Return 'unknown' if filename is empty after sanitizing

def download_file(url, local_filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

def main():
    print("Script started. Attempting to fetch records.")
    
    try:
        response = requests.get(AIRTABLE_ENDPOINT, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return
    except Exception as err:
        print(f"An error occurred: {err}")
        return
    
    print("Successfully fetched data from Airtable.")
    
    records = response.json().get('records', [])
    if not records:
        print("No records found. Exiting script.")
        return
    
    print(f"Number of records fetched: {len(records)}")
    
    for record in records:
        folder_name = record['fields'].get(FOLDER_NAME_FIELD, 'Unknown')
        sanitized_folder_name = sanitize_filename(folder_name)
        record_folder = os.path.join(DOWNLOAD_ROOT_DIR, sanitized_folder_name)
        os.makedirs(record_folder, exist_ok=True)
        
        for attachment_field in ATTACHMENT_FIELDS:
            attachments = record['fields'].get(attachment_field, [])
            if not attachments:
                print(f"No attachments found for {attachment_field} in record with name {sanitized_folder_name}.")
                continue
            
            for attachment in attachments:
                url = attachment['url']
                filename = sanitize_filename(attachment['filename'])
                local_path = os.path.join(record_folder, filename)
                
                print(f"Downloading {filename} from {attachment_field} to folder '{sanitized_folder_name}'...")
                download_file(url, local_path)

    print("All files have been downloaded.")

if __name__ == '__main__':
    main()
