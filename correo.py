import smtplib
message = "Mensaje enviado desde python"
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
print("iniciando sesión")
server.login('exulonk@gmail.com','Dr365PC2021')
server.sendmail('exulonk@gmail.com','test@doctorpclaspalmas.com', message)
server.quit()
print("correo enviado correctamente")