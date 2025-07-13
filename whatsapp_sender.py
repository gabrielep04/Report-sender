import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

def send_whatsapp_message(body: str, media_url: str = None) -> str:
    """
    Envía un mensaje de WhatsApp con el cuerpo y opcionalmente un medio.
    Devuelve el SID del mensaje.
    """
    client = Client(os.getenv('TWILIO_ACCOUNT_SID'), os.getenv('TWILIO_AUTH_TOKEN'))
    msg_kwargs = {
        'body': body,
        'from_': os.getenv('TWILIO_WHATSAPP_FROM'),
        'to':   os.getenv('TWILIO_WHATSAPP_TO')
    }
    if media_url:
        msg_kwargs['media_url'] = [media_url]
    return client.messages.create(**msg_kwargs).sid