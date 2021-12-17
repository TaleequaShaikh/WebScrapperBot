from email import message
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send(filename):
    #Email Header includes [from][to][subject]
    from_add = "ifyouknowyouknow.youbttrknow@gmail.com"
    to_add = "herofiennes3@gmail.com"
    subject = "Finance Stock Report"

    # creating msg object and attaching from, to & subject [HEADER]
    msg = MIMEMultipart()
    msg['From'] = from_add
    msg['To'] = to_add
    msg['Subject'] = subject

    #creating a message with body
    body = "<b>Today's Finance Report Attached.</b>"
    msg.attach(MIMEText(body, 'html')) # attaching "Hey there, sending mail through python!" to msg , passing body , (Plain/HTML/Xml) parameter to MIMEText
    message = msg.as_string() # converting msg to string

    #adding attachment
    my_file = open(filename, "rb")

    part = MIMEBase("application", "octet-stream")
    part.set_payload((my_file).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename= ' + filename)
    msg.attach(part)
    message = msg.as_string()

    server = smtplib.SMTP('smtp.gmail.com', 587) # smtp method(port, portid)
    server.starttls()
    server.login('ifyouknowyouknow.youbttrknow@gmail.com', 'adlsqydzknplfbtz' )
    server.sendmail(from_add, to_add,  message)
    server.quit()






