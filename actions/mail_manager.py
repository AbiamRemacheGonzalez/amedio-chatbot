import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class MailManager:

    def __init__(self):
        self.composedMessage = MIMEMultipart()
        self.composedMessage['From'] = "exulonk@gmail.com"
        self.fromPass = 'Dr365PC2021'

    def sendMailTo(self,message,toAdress,type_request,client_mail):
        #Construcción del mensaje
        self.composedMessage['Subject'] = "Presupuesto de "+type_request+" | Cliente: "+client_mail
        self.composedMessage['To'] = toAdress
        self.composedMessage.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(self.composedMessage['From'],self.fromPass)
        server.sendmail(self.composedMessage['From'],self.composedMessage['To'], self.composedMessage.as_string())
        server.quit()
        print("correo enviado correctamente")