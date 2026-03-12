import smtplib
email = "tuemail@gmail.com"
password = "tu_contraseña_de_aplicacion"

destinatarios = {
    "cliente1@gmail.com"
    "cliente2@gmail.com"
}
mensaje = """Subject: Informacion solicitada
Hola, gracias por contactarte.
Si necesitás mas info, ressponde este mensaje.
"""
with smtplib.SMTP_SSL("smt.gmail.com", 465) as smtp:
    smtp.login(email, password)
    for destinatario in destinatarios:
        smtp.sendmail(email, destinatario, mensaje)
        print("Emails enviados")