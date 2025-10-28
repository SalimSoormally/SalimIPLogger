import socket
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import pytz

# Define scopes and credentials
SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file("credentials.json", scopes=SCOPES)
client = gspread.authorize(creds)

# Optional debug: list visible sheets
print("Sheets visible to service account:")
for s in client.openall():
    print("-", s.title)

# Open your Google Sheet
sheet = client.open("SS_IP_log").sheet1

# Get your actual public IP via DNS lookup
hostname = "salimsm.ddns.net"
ip = socket.gethostbyname(hostname)
print(f"Resolved IP: {ip}")

# Use Mauritius local time for timestamp
mauritius = pytz.timezone("Indian/Mauritius")
timestamp = datetime.now(mauritius).strftime("%d/%m/%Y %H:%M:%S")

# Log timestamp and IP
sheet.append_row([timestamp, ip])
print(f"Logged IP {ip} at {timestamp}")
