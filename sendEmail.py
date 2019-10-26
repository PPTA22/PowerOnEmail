import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import datetime
import socket

hostname = socket.gethostname()
ip_addrs = socket.gethostbyname_ex(socket.gethostname())[2]

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()

    time = datetime.datetime.now()
    subject = f'{hostname}: {time.year} {time.month} {time.day}'
    # subject = MIMEText(subject, "text")

    body = f'Hostname: {hostname} \n'
    body += f'Turn on time: {time.year} {time.month} {time.day} - {time.hour}:{time.minute}  \n'
    body += f'ip address: {ip_addrs}'
    msg = MIMEMultipart()
    body = MIMEText(body, "plain")
    email_user,email_password = 'example@gmail.com', 'your_password'
    email_send = 'receiver@gmail.com'

    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject
    msg.attach(body)


    # msg.attach(MIMEText(body))

    server.starttls()
    print('[!] about to login')
    server.login(email_user,email_password)
    print('[+] login success')
    # server.sendmail(email_user,email_send, msg.as_string())
    server.sendmail(email_user,email_send, msg.as_string())
    print('[+] sent email')
    server.quit()

except Exception as e:
    print(e)
    print ('Something went wrong...')


# sc.exe create sendEmail binPath= "C:\sendEmail.exe"
# sc.exe delete sendEmail
