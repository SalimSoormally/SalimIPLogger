import requests
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file("credentials.json", scopes=SCOPES)
client = gspread.authorize(creds)
# Debug: List all accessible sheets
print("Sheets visible to service account:")
for s in client.openall():
    print("-", s.title)

sheet = client.open("SS_IP_log").sheet1

response = requests.get("https://ipinfo.io/json")
print("Raw response:", response.text)  # Optional debug
ip = response.json()["ip"]
timestamp = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
sheet.append_row([timestamp, ip])
print(f"Logged IP {ip} at {timestamp}")
