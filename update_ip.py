
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Define Google API scopes
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Load credentials and authorize client
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", SCOPES)
client = gspread.authorize(creds)

# Open the Google Sheet
sheet = client.open("SS_IP_Log").sheet1

# Fetch current public IP
try:
    ip = requests.get("https://api.ipify.org").text
except Exception as e:
    print(f"Error fetching IP: {e}")
    exit(1)

# Prepare timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Find the next empty row
next_row = len(sheet.get_all_values()) + 1

# Update the sheet: Column A = Timestamp, Column B = IP
try:
    sheet.update_cell(next_row, 1, timestamp)
    sheet.update_cell(next_row, 2, ip)
    print(f"Updated row {next_row} with IP: {ip}")
except Exception as e:
    print(f"Error updating Google Sheet: {e}")
    exit(1)
``
