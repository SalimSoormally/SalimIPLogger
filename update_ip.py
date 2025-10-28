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
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Run dig instead of nslookup
result = subprocess.run(["dig", "+short", "salimsm.ddns.net"], capture_output=True, text=True)
ip_address = result.stdout.strip()

if ip_address:
    sheet.append_row([timestamp, ip_address])
    print(f"Logged: {timestamp} - {ip_address}")
else:
    print("IP address not found.")
