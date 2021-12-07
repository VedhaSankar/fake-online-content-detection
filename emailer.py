
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
from email.mime.application import MIMEApplication
import os
from os.path import basename

load_dotenv()

sender_address = os.environ.get('GMAIL_USER') 
sender_pass = os.environ.get('GMAIL_PASSWORD')

smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()
smtp.login(sender_address, sender_pass)


msg = MIMEMultipart()
msg['Subject'] = "subject"
msg.attach(MIMEText("look what you made me do"))


# img_data = open(one_img, 'rb').read()
# msg.attach(MIMEImage(img_data, 
#                      name=os.path.basename(one_img)))


to = ["ishitagops12@gmail.com" , " vedhasankar26@gmail.com", "harenemaharajan02@gmail.com"]
smtp.sendmail(from_addr="Your Login Email",
              to_addrs=to, msg=msg.as_string())
smtp.quit()

print ("Email sent!")