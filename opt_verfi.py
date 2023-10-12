import random
import math
import smtplib

digits = '0123456789'
OTP = ""

# Generate a 6-digit OTP
for i in range(6):
    OTP += random.choice(digits)

# Compose the email message
otp_message = OTP + " is your OTP"

# SMTP setup
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "ms096060@gmail.com"  # Replace with your Gmail email address
sender_password = "yyjammmelxcqyzof"  # Replace with your Gmail password which is genrated by google app password

# Create an SMTP object
sending = smtplib.SMTP(smtp_server, smtp_port)
sending.starttls()

# Login to your Gmail account
sending.login(sender_email, sender_password)

# Get the user's email address
user_email = input("Enter your Email: ")

# Send the OTP to the user's email
sending.sendmail(sender_email, user_email, otp_message)

# Get the user's input for OTP verification
user_input = input("Enter your 6 digits OTP: ")

# Check if the provided OTP is correct
if user_input == OTP:
    print("OTP is correct")
else:
    print("Your OTP is not correct")

# Close the SMTP connection
sending.quit()
