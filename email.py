# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import smtplib

# message = MIMEMultipart('alternative')
# message['Subject'] = 'Test'
# message['From'] = 'test@doctorpclaspalmas.com'
# message['To'] = 'tomasmorales@doctorpclaspalmas.com'

# message.attach(MIMEText('# A Heading\nSomething else in the body', 'plain'))
# message.attach(MIMEText('<h1 style="color: blue">A Heading</a><p>¿FUCIONARA?</p>', 'html'))

# server = smtplib.SMTP('smtp.ionos.com', 587)
# server.starttls()
# server.login('test@doctorpclaspalmas.com', 'Dr365PC2021')
# server.sendmail('test@doctorpclaspalmas.com', 'tomasmorales@doctorpclaspalmas.com', message.as_string())
# server.quit()

# import email_to

# server = email_to.EmailServer('smtp.ionos.com', 587, 'test@doctorpclaspalmas.com', 'Dr365PC2021')
# server.quick_email('tomasmorales@doctorpclaspalmas.com', 'Test',
#                    ['# A Heading', 'Something else in the body'],
#                    style='h1 {color: blue}')

import smtplib
message = "Mensaje enviado desde python"
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
print("iniciando sesión")
server.login('exulonk@gmail.com','Dr365PC2021')
server.sendmail('exulonk@gmail.com','tomasmorales@doctorpclaspalmas.com', message)
server.quit()
print("correo enviado correctamente")