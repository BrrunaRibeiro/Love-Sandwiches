import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("love_sandwiches")

def get_sales_data():
    """
    Gets sales data from the user with the input function.
    """
    print("Please enter the sales data from the last market")
    print("Data should be 5 numbers, sepparated by commas")
    print("Example: 10,20,30,40,50,60")

    data_str = input("Enter you data here: \n")
    
    sales_data = data_str.split(',')

get_sales_data()