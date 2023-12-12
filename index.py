import requests
import time

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def fetch_api_data(api_url):
    try:
        # Making a GET request to the API
        response = requests.get(api_url)

        # Checking if the request was successful (status code 200)
        if response.status_code == 200:
            # Parsing and returning the JSON response
            return response.json()
        else:
            # Printing an error message if the request was not successful
            print(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'your_api_url_here' with the actual API URL
api_url = 'https://self-service.dal.ca/BannerExtensibility/internalPb/virtualDomains.dal_stuweb_academicTimetable?MTk%3DdGVybXM%3D=NTk%3DMjAyNDIwOw%3D%3D&MjQ%3DcGFnZV9udW0%3D=OTU%3DMQ%3D%3D&NA%3D%3DbWF4=MjE%3DMTAwMA%3D%3D&NTM%3Db2Zmc2V0=NDk%3DMA%3D%3D&NTY%3DZGlzdHJpY3Rz=ODg%3DMTAwOw%3D%3D&NjM%3DY3JzZV9udW1i=NTU%3Dnull&Njg%3Dc3Vial9jb2Rl=MzA%3DQ1NDSQ%3D%3D&ODc%3DcGFnZV9zaXpl=NzE%3DOTk5OQ%3D%3D&encoded=true'

def send_email(mobile_data):
    # Email configuration
    sender_email = "noreplytripify@gmail.com"
    receiver_email = "singhjaskaran762@gmail.com"
    subject = "Mobile Computing available"
    body = mobile_data['PERC_FULL']

    # Create the MIME object
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Attach the body to the email
    message.attach(MIMEText(body, "plain"))

    # Establish a connection to the SMTP server (in this case, Gmail's SMTP server)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create a connection to the server
    server = smtplib.SMTP(smtp_server, smtp_port)

    # Start the TLS connection (for security)
    server.starttls()

    # Login to your email account
    email_password = "aizridyhtghdmpww"
    server.login(sender_email, email_password)

    # Send the email
    server.sendmail(sender_email, receiver_email, message.as_string())

    # Quit the server
    server.quit()

while True:
    # Call the function and store the response data
    time.sleep(1)
    api_data = fetch_api_data(api_url)

    # Print or process the response data as needed
    print(api_data[184])

    # Access the specific data you need directly
    mobile_data = api_data[184]

    if mobile_data['PERC_FULL'] != 'FULL' or mobile_data['CRSE_TITLE'] != 'Mobile Computing':
        print('hi')
        send_email(mobile_data)
        time.sleep(60)
