import smtplib

gmail_user = 'programtesting082021@gmail.com'
pwd = 'MacSteve2000417'


sent_from = gmail_user
to = 'jackliang0417@gmail.com'
subject = 'Testing Email'
body = 'This is a testing email sent by python'

email_text =  """\

From: %s
To: %s
Subject: %s

%s
"""%(sent_from, to, subject, body)


def send(text):
    try:
        smpt = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smpt.ehlo()
        smpt.login(gmail_user, pwd)
        smpt.sendmail(sent_from, to, text)
        #smpt.sendmail(sent_from, to, email_text)
        smpt.close()
        print("Sent")
    except Exception as ex:
        print("Something is wrong", ex)

# send()

