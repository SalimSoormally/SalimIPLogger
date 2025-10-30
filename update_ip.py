import socket
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import pytz

# Define scopes and credentials
SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file("credentials.json", scopes=SCOPES)
client = gspread.authorize(creds)

# Open your Google Sheet
sheet = client.open("SS_IP_log").sheet1

# Get your actual public IP via DNS lookup
hostname = "salimsm.ddns.net"
try:
    ip = socket.gethostbyname(hostname)
except socket.gaierror:
    print("DNS lookup failed. Skipping append.")
    ip = None

# Use Mauritius local time for timestamp in ISO format
mauritius = pytz.timezone("Indian/Mauritius")
timestamp = datetime.now(mauritius).strftime("%Y-%m-%d %H:%M:%S")

# Append only if IP is valid
if ip:
    sheet.append_row([timestamp, ip])
    print(f"Logged IP {ip} at {timestamp}")
else:
    print("No IP logged due to DNS failure.")
