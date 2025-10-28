import requests
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# Define scope for Google Sheets API
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# Load credentials from file
creds = Credentials.from_service_account_file("credentials.json", scopes=SCOPES)

# Authorize client
client = gspread.authorize(creds)

# Open the Google Sheet by name
sheet = client.open("SS_IP_Log").sheet1

# Get current public IP
ip = requests.get("https://api.ipify.org").text.strip()

# Get current timestamp
timestamp = datetime.now().strftime("%m/%d/%Y %H:%M:%S")

# Append row to sheet
sheet.append_row([timestamp, ip])

# Optional: print confirmation to GitHub Actions log
print(f"Logged IP {ip} at {timestamp}")
