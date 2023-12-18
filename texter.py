import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

#Get sensitive info
creds = {"email": "", "password": "", "phone_num": ""}
credfile = open("texter_creds.txt")
for key in creds:
	creds[key] = credfile.readline()
credfile.close()

#Define constants
sms_gateway_end = "@vzwpix.com"
sms_gateway = creds["phone_num"] + sms_gateway_end

smtp = "smtp.gmail.com"
port = 587

#start the service
server = smtplib.SMTP(smtp, port)
server.starttls()
server.login(creds["email"],creds["password"])


#Create the message
msg = MIMEMultipart()
msg['From'] = creds["email"]
msg['To'] = sms_gateway
msg['Subject'] = "Alert"
body = "Someone in your room\n"
msg.attach(MIMEText(body, 'plain'))

#Attach image
fp = open('/home/pi/Python/TextSender/burger2.jpg', 'rb')
msg_img = MIMEImage( fp.read())
fp.close()
msg.attach(msg_img)

#Send the sms
server.sendmail("", sms_gateway, msg.as_string())
