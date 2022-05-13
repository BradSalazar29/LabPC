import getpass
import smtplib
import ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-c', help='ingree el cuerpo del correo')
parser.add_argument('-a', help='Ingrese el asunto del correo')
parser.add_argument('-d', help='Ingrese a quien enviara el correo')
parse = parser.parse_args()

correo_personal = input('ingresa tu correo: ')
contra = getpass.getpass(prompt='Cual es tu password: ')
correo_destino = parse.d
asunto_correo = parse.a
cuerpo_correo = parse.c

mensaje = MIMEMultipart()
mensaje["From"] = correo_personal
mensaje["To"] = correo_destino
mensaje["Subject"] = asunto_correo

mensaje.attach(MIMEText(cuerpo_correo, "plain"))

text = mensaje.as_string()

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(correo_personal, contra)
    server.sendmail(correo_personal, correo_destino, text)
