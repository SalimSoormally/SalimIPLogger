
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Google API scopes for Sheets and Drive
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Load credentials and authorize gspread client
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", SCOPES)
client = gspread.authorize(creds)

# Open the Google Sheet by name
SHEET_NAME = "SS_IP_Log"  # Make sure this matches your sheet name
sheet = client.open(SHEET_NAME).sheet1

# Fetch current public IP
try:
    ip = requests.get("https://api.ipify.org").text
except Exception as e:
    print(f"Error fetching IP: {e}")
    exit(1)

# Prepare timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Find next empty row
next_row = len(sheet.get_all_values()) + 1

# Update the sheet: Column A = Timestamp, Column B = IP
try:
    sheet.update_cell(next_row, 1, timestamp)
    sheet.update_cell(next_row, 2, ip)
    print(f"Updated row {next_row} with IP: {ip}")
except Exception as e:
    print(f"Error updating Google Sheet: {e}")
    exit(1)
