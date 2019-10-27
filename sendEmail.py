import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import datetime
from time import sleep
import socket
sleep(25) # In case the router/ dhcp responde lately
time = datetime.datetime.now()

try:
    hostname = socket.gethostname()
    ip_addrs = socket.gethostbyname_ex(socket.gethostname())[2]
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()


    subject = f'{hostname}: {time.year} {time.month} {time.day}'
    # subject = MIMEText(subject, "text")

    body = f'Hostname: {hostname} \n'
    body += f'Turn on time: {time.year} {time.month} {time.day} - {str(time.hour).zfill(2)}:{time.minute}  \n'
    body += f'ip address: {ip_addrs}'
    msg = MIMEMultipart()
    body = MIMEText(body, "plain")
    email_user,email_password = 'example@email.com', 'your_pwd'
    email_send = 'receiver_example@email.com'

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

# pyinstaller -F sendEmail.py
# sc.exe create sendEmail binPath= "C:\sendEmail.exe"
# sc.exe delete sendEmail
# remeber to choose automatic start in service tab

'''
Wnat new function
- use txt as .ini config file, easy to modified email, such info
- send including the real ip, not only the NAT ip
- if network down, hold the service, until internet goup

'''
