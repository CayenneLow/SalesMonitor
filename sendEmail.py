from login import username, password
import smtplib

def sendEmail(price, link):
    sent_from = username
    to = 'lowkhyeean@gmail.com'
    subject = "Get dem headphones boi"
    body = "Price is {} at {}".format(price, link)

    message = "From: %s\r\n" % sent_from + "To: %s\r\n" % to + "Subject: %s\r\n" % subject + "\r\n" + body
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(username, password)
        server.sendmail(sent_from, to, message)
        server.close()

        print("Email sent")
    except Exception as e:
        print(e)

