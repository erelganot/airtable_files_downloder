# Airtable Attachment Downloader

This Python script automatically downloads all attachments from specified fields within an Airtable base, organizing them into directories named after a chosen field from each record.

## Description

This script interacts with the Airtable API, retrieving records from a specified table. It then downloads all the attachments found in the designated fields, storing them into neatly organized folders. This is particularly useful for users looking to backup their Airtable attachments locally or to migrate data to another service.

## Features

- Connects to Airtable API to retrieve table records.
- Downloads attachments from a user-defined list of fields.
- Organizes downloaded files into folders named according to a specific field value from each record.
- Filename sanitization ensures compatibility with Windows and Unix file systems.

## Prerequisites

Before using this script, you should have the following setup ready:

- Python 3.x installed.
- `requests` library installed in your Python environment (can be installed via pip).

## Installation

1. Clone this repository or download the `airtable_attachment_downloader.py` script to your local machine.
2. Install the `requests` Python library:

   ```bash
   pip install requests


## Update the script with your Airtable credentials and settings:

API_KEY = 'your_api_key'
BASE_ID = 'your_base_id'
TABLE_NAME = 'your_table_name'


Modify the ATTACHMENT_FIELDS list to include the fields that contain the attachments you want to download.

Set the DOWNLOAD_ROOT_DIR to your desired download location.

## Usage
To run the script, execute it from the command line:
python airtable_attachment_downloader.py

The script will create directories corresponding to each record and download all associated attachments to their respective directories.

## Contributing
Contributions are welcome! If you have suggestions for improvements or bug fixes, please feel free to fork this repository, make changes, and submit a pull request.

## License

This project is open-sourced under the this files License. See the LICENSE file for more information.


## Disclaimer
The provided script is on an "as-is" basis. The author is not responsible for any damages or losses that may arise from its use.

## Support
Should you encounter any issues or have questions regarding this script, please file an issue on the GitHub repository.

## Acknowledgments
Gratitude to the creators and maintainers of the Airtable API.
This project was inspired by the needs of the Airtable community for better data management tools.
