"""
Envío de emails transaccionales.
- Componer un email con HTML y texto plano (multipart)
- Enviarlo por SMTP
- Plantillas simples con variables
En producción se usa un proveedor (Resend, SendGrid) por su API o SMTP;
la forma de componer el mensaje es la misma. Config por variables de entorno.
"""
import os
import smtplib
from email.message import EmailMessage

SMTP_HOST = os.getenv("SMTP_HOST", "localhost")
SMTP_PORT = int(os.getenv("SMTP_PORT", "8025"))
SMTP_USER = os.getenv("SMTP_USER", "")
SMTP_PASS = os.getenv("SMTP_PASS", "")
FROM = os.getenv("EMAIL_FROM", "Sabores del Barrio <hola@sabores.com>")


def componer(destino: str, asunto: str, html: str, texto: str) -> EmailMessage:
    msg = EmailMessage()
    msg["From"] = FROM
    msg["To"] = destino
    msg["Subject"] = asunto
    msg.set_content(texto)                 # versión texto plano (fallback)
    msg.add_alternative(html, subtype="html")  # versión HTML
    return msg


def enviar(msg: EmailMessage):
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as s:
        if SMTP_USER:                      # en producción, con auth y TLS
            s.starttls()
            s.login(SMTP_USER, SMTP_PASS)
        s.send_message(msg)


# ---------- Plantillas ----------
def email_confirmacion_pedido(destino: str, pedido_id: int, total: float):
    html = f"""\
<h2>¡Gracias por tu pedido!</h2>
<p>Tu pedido <b>#{pedido_id}</b> fue confirmado.</p>
<p>Total: <b>${total:,.0f}</b></p>
<p>Te avisamos cuando esté listo.</p>"""
    texto = (f"Gracias por tu pedido!\n"
             f"Pedido #{pedido_id} confirmado. Total: ${total:,.0f}\n")
    return componer(destino, f"Pedido #{pedido_id} confirmado", html, texto)


def email_reset_password(destino: str, link: str):
    html = f'<p>Para cambiar tu contraseña, entrá acá:</p><p><a href="{link}">{link}</a></p><p>El link vence en 1 hora. Si no lo pediste, ignoralo.</p>'
    texto = f"Cambiar contraseña: {link}\nVence en 1 hora. Si no lo pediste, ignoralo.\n"
    return componer(destino, "Restablecer contraseña", html, texto)
