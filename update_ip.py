
import subprocess
import datetime
import gspread
from google.oauth2.service_account import Credentials

# Google Sheets setup
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json", scopes=SCOPES)
client = gspread.authorize(creds)

# Your Google Sheet name
SHEET_NAME = "SS_IP_Log"
sheet = client.open(SHEET_NAME).sheet1

# Get current timestamp
timestamp = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")

# Run nslookup
result = subprocess.run(["nslookup", "salimsm.ddns.net"], capture_output=True, text=True)
lines = result.stdout.splitlines()

# Extract IP address (last line usually contains it)
ip_address = None
for line in lines:
    if "Address:" in line:
        ip_address = line.split("Address:")[-1].strip()

# Append to Google Sheet
if ip_address:
    sheet.append_row([timestamp, ip_address])
    print(f"Logged: {timestamp} - {ip_address}")
else:
    print("IP address not found.")
