import json
from google.oauth2.credentials import Credentials
import gspread
from google_auth_oauthlib.flow import InstalledAppFlow

# Google Sheets API token obtained from Google Sign-In
GS_TOKEN = {"token": "Your Token Which You got from Google Sign in"}

# Define the scope for Google Drive API
SCOPES = ['https://www.googleapis.com/auth/drive']

# Authenticate the Google account and obtain credentials


def authenticate_google_account_for_spreadsheet():
    """
    Authenticate the user's Google account to access Google Sheets.
    This function initiates a local server for OAuth 2.0 authorization
    and generates a token that can be used to access Google Sheets.

    Returns:
        Credentials object containing the authenticated user's access token.
    """
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', SCOPES)
    token = flow.run_local_server(port=8001)
    return token


def fetch_data_from_google_sheet(gs_token, gs_sheet_url):
    """
    Fetch data from a Google Sheet given a valid token and sheet URL.

    Args:
        gs_token (dict): A dictionary containing the Google Sheets API token.
        gs_sheet_url (str): The URL of the Google Sheet to be accessed.

    Returns:
        list: A list of dictionaries where each dictionary represents a row in the sheet.
    """
    # Check if the token and sheet URL are provided
    if gs_token and gs_sheet_url:
        # Convert the token into credentials
        credentials = Credentials.from_authorized_user_info(gs_token, SCOPES)
        # Authorize the gspread client with the obtained credentials
        gc = gspread.authorize(credentials)
        # Open the Google Sheet by its URL
        sh = gc.open_by_url(gs_sheet_url)
        # Select the first worksheet in the sheet
        worksheet = sh.sheet1
        # Fetch all values from the worksheet
        values = worksheet.get_all_values()
        # Convert the sheet rows into a list of dictionaries
        header = values[0]
        data_dicts = [dict(zip(header, row)) for row in values[1:]]
        return data_dicts
    else:
        return "No Token or Sheet URL Found"


# Example usage
g_token = GS_TOKEN
g_sheet_url = "Your Google Sheet Url"
print(fetch_data_from_google_sheet(g_token, g_sheet_url))
