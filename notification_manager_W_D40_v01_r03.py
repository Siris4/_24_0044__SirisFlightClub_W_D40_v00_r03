
# can send SMS and emails, based on data in a Google sheet:

import os
import requests
from twilio.rest import Client
import gspread
import smtplib

# this class is responsible for sending SMS notifications with the deal flight details.
    # def check_if_Google_sheet_is_lowest_price(self):

# retrieve Twilio credentials and phone numbers from environment variables:
class NotificationManager:
    def __init__(self):
        # for twilio sms sending:
        self.account_sid = os.environ.get("ACCOUNT_SID")
        self.auth_token = os.environ.get("AUTH_TOKEN")
        self.from_your_virtual_twilio_phone_number = os.environ.get("FROM_YOUR_VIRTUAL_TWILIO_PHONE_NUMBER")
        self.to_recipient_phone_number = os.environ.get("TO_RECIPIENT_PHONE_NUMBER")
        self.client = Client(self.account_sid, self.auth_token)

# class NotificationManager:
#     def __init__(self):
#         self.client = Client(account_sid, auth_token)   # for Twilio SMS sending:

    # def send_an_sms_text(self, message):
    #     pass
    #     # --------------------------------------- TAKE THESE OUT WHEN TESTING PHASE IS ALL FINISHED ---------------------------------------------- #
    #     print(f"account_sid = {account_sid}")
    #     print(f"auth_token = {auth_token}")
    #     print(f"FROM_YOUR_VIRTUAL_TWILIO_PHONE_NUMBER = {from_your_virtual_twilio_phone_number}")
    #     print(f"TO_RECIPIENT_PHONE_NUMBER = {to_recipient_phone_number}")
    #     # ---------------------------------------------------------------------------------------------------------------------------------------- #
    #
    #     # check if all required variables were retrieved:
    #     if not all([account_sid, auth_token, from_your_virtual_twilio_phone_number, to_recipient_phone_number]):
    #         print("Error: One or more environment variables are not set.")
    #     else:
    #         try:
    #             # initialize Twilio client:
    #             client = Client(account_sid, auth_token)
    #
    #             # compose and send the message:
    #             message = self.client.messages.create(
    #                 body=message,
    #                 from_=from_your_virtual_twilio_phone_number,
    #                 to=to_recipient_phone_number,
    #                 # to='recip_ph_number',  #toggle this on and the one below this toggled off, to easily swap phone numbers
    #             )
    #
    #             # print the message status:
    #             print(f"Message Status: {message.status}. Yes, the text got sent :)")
    #             print(f"The message.sid: {message.sid}")
    #         except Exception as e:
    #             print(f"Failed to send message: {e}")

    # google API name: 'convert sheet data to dict'
    def convert_google_sheet_names_and_emails_to_dict(self):
        import gspread

        # assuming you've already downloaded your service account key JSON file and it's located at the specified path
        json_key_file_path = r'C:\Users\guber\Desktop\CoDex\Python\GitHub-Python-Files\_24_0044__Day40_Flight_Club_Customer_Emails_Capstone_Proj_Part2__240215\__P1_Project_Name_NWY_D##_v##_r##\_Gen Plygrd\Venv\_v01s\r00-r09\v01_r03\DONT POST\advance-archery-414723-c0e6.json'

        # authenticate using the service account file
        gc = gspread.service_account(filename=json_key_file_path)

        # open the spreadsheet by name
        spreadsheet = gc.open("SirisFlightDeals")

        # now, access the specific sheet within the spreadsheet by its name
        sheet = spreadsheet.worksheet("users")  # This accesses the sheet named "users"

        # fetch all the data in the sheet into a list of dictionaries
        data = sheet.get_all_records()

        # print the fetched data
        for row in data:
            print(row)  # Each row is a dictionary with keys based on your sheet's column names

        return data


            # gc = gspread.service_account()
            #
            # # Open a sheet from a spreadsheet in one go
            # wks = gc.open("Where is the money Lebowski?").sheet1
            #
            # # Update a range of cells using the top left corner address
            # wks.update('A1', [[1, 2], [3, 4]])
            #
            # # Or update a single cell
            # wks.update('B42', "it's down there somewhere, let me take another look.")
            #
            # # Format the header
            # wks.format('A1:B1', {'textFormat': {'bold': True}})

    def send_emails_to_customers(self):
        import smtplib, os
        # import datetime as dt

        customers = self.convert_google_sheet_names_and_emails_to_dict()

        my_from_email1 = os.environ.get("MY_FROM_EMAIL1")
        password = os.environ.get("PASSWORD")

        # their_email2 = "Test2.Omega2000@yahoo.com"

        with smtplib.SMTP("smtp.gmail.com",
                          port=587) as connection:  # allows us to connect to our email provider's SMTP email server, and create an Object from the .SMTP(Class), location of the server (gmail = smtp.gmail.com)
            connection.starttls()  # tls = Transport Layer Security, a way of securing our connection to our email server. (encrypted and secure)) (indent block starts here)
            connection.login(user=my_from_email1, password=password)

            for customer in customers:
                first_name = customer['First Name']  # Adjust based on your column name
                their_email2 = customer['Email']  # Adjust based on your column name
                email_subject = "Personalized Greeting!"
                email_body = f"Hello {first_name},\n\nThis is a personalized message from Siris Flight Deals."
                email_message = f"Subject:{email_subject}\n\n{email_body}"

            connection.sendmail(
                from_addr=my_from_email1,
                to_addrs=their_email2,
                msg=email_message
            )
            print(f"Email sent to {their_email2}")

            # connection.sendmail(from_addr=my_from_email1,
            #                     to_addrs=their_email2,
            #                     msg="Subject:Hello, this is the Subject field3!!\n\nThis is the body of my Python Email3."
                                # (indent block ends here.)
                                # )  # subject field goes inside the msg=parameter: + \n\n
        # instead of connection.close() to close out the end of the email sending code, we can use the same trick as our files, by adding "with smtplib... as connection: (and then indent the rest of the code in the block above)

        # one of the biggest errors is manually typing things out into the strings above, instead of just imported them into the code.
