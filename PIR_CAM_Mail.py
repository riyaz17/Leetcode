import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import RPi.GPIO as GPIO
import picamera

# Email account details
from_email = "annamkeshava8554@gmail.com"
to_email = "lavanyasg2822@gmail.com"
password = "pyanfugpfpmdypno"

# PIR sensor setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

# Camera setup
camera = picamera.PiCamera()

while True:
    if GPIO.input(4):
        print("Motion detected!")
        # Capture an image
        camera.capture('image.jpg')
        
        # Create the message
        msg = MIMEMultipart()
        msg["From"] = from_email
        msg["To"] = to_email
        msg["Subject"] = "Intrusion Alert"
        body = "Intrusion detected! Image attached"
        msg.attach(MIMEText(body, "plain"))

        # Open the image file
        with open("image.jpg", "rb") as img_file:
            img_data = img_file.read()

        # Attach the image to the email
        image = MIMEImage(img_data, name="image.jpg")
        msg.attach(image)
        # Connect to the SMTP server and send the email
        smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
        smtp_server.starttls()
        smtp_server.login(from_email, password)
        smtp_server.sendmail(from_email, to_email, msg.as_string())
        smtp_server.quit()
    time.sleep(1)

