# import package
import africastalking

from dotenv import load_dotenv
import os
load_dotenv()


def send_sms_notification( message, to_phone):
    try:
        # Initialize SDK
        username= os.getenv("AT_USER_NAME")   # use 'sandbox' for development in the test environment
        api_key= os.getenv("AT_API_KEY")    # use your sandbox app API key for development in the test environment
        africastalking.initialize(username, api_key)

        # Initialize a service e.g. SMS
        sms = africastalking.SMS

        # Use the service synchronously
        response = sms.send(message, to_phone) # Phone must start with +254XXX

        print("Success sending sms ",response)
        return True

        # # Or use it asynchronously
        # def on_finish(error, response):
        #     if error is not None:
        #         raise error
        #     print(response)

        # sms.send("Hello Message!", ["+2547XX"], callback=on_finish)  

    except Exception as e:
        print ("Error sending sms ", e)
        return False

if __name__ == '__main__':
    send_sms_notification("Hello Message!", ["+254110456655"])



