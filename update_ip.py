import requests
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import os
import sys

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

KEYFILE = "credentials.json"
SPREADSHEET_NAME = "SS_IP_Log"

if not os.path.exists(KEYFILE):
    print("Credentials file not found:", KEYFILE)
    sys.exit(1)

creds = Credentials.from_service_account_file(KEYFILE, scopes=SCOPES)
client = gspread.authorize(creds)

try:
    sheet = client.open(SPREADSHEET_NAME).sheet1
except Exception as e:
    print("Error opening spreadsheet:", e)
    sys.exit(1)

try:
    ip = requests.get("https://api.ipify.org", timeout=10).text.strip()
except Exception as e:
    print("Error fetching IP:", e)
    sys.exit(1)

timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
try:
    next_row = len(sheet.get_all_values()) + 1
    sheet.update_cell(next_row, 1, timestamp)
    sheet.update_cell(next_row, 2, ip)
    print(f"Updated row {next_row} with IP: {ip}")
except Exception as e:
    print("Error updating Google Sheet:", e)
    sys.exit(1)
