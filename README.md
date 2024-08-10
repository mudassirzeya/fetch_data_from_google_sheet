# Google Sheets Data Fetcher using gspread in Python
This project provides a simple Python script to fetch data from a Google Sheet using the gspread library and Google OAuth 2.0 for authentication.

# Features
1) Authenticate your Google account to access Google Sheets.
2) Fetch data from a specific Google Sheet using its URL.
3) Convert the fetched data into a list of dictionaries for easy data manipulation.

# Prerequisites
1) Python 3.6 or higher.
2) A Google Cloud project with the Google Sheets API and Google Drive API enabled.
3) OAuth 2.0 credentials file (credentials.json) from the Google Cloud Console.

# Installation
1) git clone https://github.com/mudassirzeya/fetch_data_from_google_sheet.git
2) myenv\Scripts\activate to get into virtual environment

# Note
1) I have not provided the credentials.json file. You can obtain it from Google Cloud Console by enabling the Google Drive API and Google Sheets API, and then creating the credentials.

# Usage
1) Authenticate Google Account
   Run the following function to authenticate your Google account and generate a token for accessing Google Sheets:
   ![image](https://github.com/user-attachments/assets/873f2a02-8239-4aba-9df8-050815a4ca69)

2) Fetch Data from Google Sheet
   Use the fetch_data_from_google_sheet function to fetch data from a Google Sheet:
   ![image](https://github.com/user-attachments/assets/494cf6f0-97ba-4b7f-9f2a-4d61d130a34c)

# Example
  Here's a simple example of how to use the script to fetch data:
  ![image](https://github.com/user-attachments/assets/141236af-60f5-43e1-9885-fc6995f50118)




