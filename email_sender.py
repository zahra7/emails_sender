import smtplib

to = input("Enter the Email of the recipient : ")

content = input("Enter the content of the email : ")

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    #You have to Turn 'Allow less secure apps' to ON
    #Replace the sender email and password
    server.login("senderemail@gmail.com", "senderpassword")
    server.sendmail("senderemail@gmail.com", to, content)
    server.close()

sendEmail(to, content)