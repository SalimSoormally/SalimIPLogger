import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the required scopes for Google Sheets and Drive
scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Load credentials from the JSON file
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scopes)

# Authorize the client
client = gspread.authorize(creds)

# Open the Google Sheet by name
sheet = client.open("SS_IP_Log").sheet1

# Example: Update cell A1 with new IP
sheet.update_cell(1, 1, "New IP Address")
