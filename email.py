
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import os

smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()
smtp.login('yoursfakely@gmail.com', 'yoyomanthan987')


msg = MIMEMultipart()
msg['Subject'] = subject
msg.attach(MIMEText(text))


# img_data = open(one_img, 'rb').read()
# msg.attach(MIMEImage(img_data, 
#                      name=os.path.basename(one_img)))


to = ["ishitagops12@gmail.com" , " harenemaharajan02@gmail.com "]
smtp.sendmail(from_addr="Your Login Email",
              to_addrs=to, msg=msg.as_string())
smtp.quit()
