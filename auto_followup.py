import smtplib
import csv
email = "tuemail@gmail.com"
password = "tu_contraseña_de_aplicacion"

with open("clientes.csv", newline='') as archivo:
    lector = csv.DictReader(archivo)
    with smtplib.SMTP_SSL("smatp.gmail.com", 465) as smtp:
        smtp.login(email, password)

        for fila in lector:
            nombre = fila["nombre"]
            destinatario = fila["email"]
            mensaje = f"""Subject:
Informacion
Hola {nombre},
Gracias por tu interes. si tenes dudas,
responde este email."""

            smtp.sendmail(email, destinatario, mensaje)
print("seguimiento enviado")             