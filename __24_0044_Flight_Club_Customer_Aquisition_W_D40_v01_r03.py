import os
import requests

# from dotenv import load_dotenv

class Intro:
    def __init__(self):
        # loads the .env file's variables
        # load_dotenv()

        # now try accessing the environment variable
        self.USERS_POST_ENDPOINT = os.environ.get('USERS_POST_ENDPOINT')
        self.SHEETY_BEARER_TOKEN = os.environ.get('SHEETY_BEARER_TOKEN', 'Sheety bearer token does not exist')
        self.headers = {"Authorization": f"Bearer {self.SHEETY_BEARER_TOKEN}", "Content-Type": "application/json"}

    def intro(self):
        # print(f"Endpoint url: {self.USERS_POST_ENDPOINT}")
        print()
        print("Welcome to the Siris Flight Club!\nWe find the best flight deals and email you.")

        first_name = input("What is your first name? \n")
        last_name = input("What is your last name? \n")
        new_user_email = input("What is your email? \n")
        new_user_email_check = input("Please type your email again: \n")

        if new_user_email == new_user_email_check:
            print("Congratulations!! You are now officially in the Siris Flight Club! Welcome!")
            self.email = new_user_email  # it's better to use 'new_user_email' as it's already checked for equality.

            # corrected payload structure
            payload = {
                "user": {
                    "firstName": first_name,
                    "lastName": last_name,
                    "email": self.email
                }
            }

            users_post_response = requests.post(url=self.USERS_POST_ENDPOINT, headers=self.headers,
                                                json=payload)  # to pass the payload with the proper 'json' parameter structure
            print(users_post_response.text)

        else:
            print("Those 2 entered emails do not match. Please try again.")


# to run this module optionally (we don't need this file, in order for the other 5 files to work)
# it can be ran once, to enter data into the google sheet, without doing it manually:
# if __name__ == "__main__":
#     intro = Intro()

