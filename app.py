# import smtplib

# driver = smtplib.SMTP('smtp.gmail.com', 587)

# driver.starttls()

# driver.login('epeetec@gmail.com', 'cmyxyorzzpiuuiwo')

# driver.sendmail('epeetec@gmail.com,', 'nathanielmusa3@gmail.com', 'Hello brother')
# print("email send succesfully ")



# import smtplib

# def sendmail(sendermail, recvmail, password, message):
#     driver = smtplib.SMTP('smtp.gmail.com', 587)
#     driver.starttls()
#     driver.login(sendermail, password)
#     driver.sendmail(sendermail, recvmail, message)
#     print("Success!!!!")

# sendmail('epeetec@gmail.com', 'nathanielmusa3@gmail.com', 'cmyxyorzzpiuuiwo', 'this mail was sent using a function')


# import smtplib
# from email.message import EmailMessage

# msg = EmailMessage()

# msg.set_content("this is just the body of the message")

# msg["subject "] = "A Robotic Email"
# msg["From"] = "epeetec@gmail.com"
# msg["To"] = "nathanielmusa3@gmail.com"

# driver = smtplib.SMTP('smtp.gmail.com', 587)
# driver.starttls()
# driver.login('epeetec@gmail.com', 'cmyxyorzzpiuuiwo')

# driver.send_message(msg)


import smtplib
from email.message import EmailMessage

def emailMessage(body, subject, sender, reciever, sender_password):

     msg = EmailMessage()

     msg.set_content(body)
     msg["subject"] = subject
     msg["From"] = sender
     msg["To"] = reciever
     
     driver = smtplib.SMTP('smtp.gmail.com', 587)

     driver.starttls()
     driver.login(sender, sender_password)
     driver.send_message(msg)

     print("Email sent successfully")



body = "This is me writing fuction that will send emails"
subject = "email sender function"
sender = "epeetec@gmail.com"
reciever = "nathanielmusa3@gmail.com"
sender_password = "cmyxyorzzpiuuiwo"

emailMessage(body, subject, sender, reciever, sender_password)