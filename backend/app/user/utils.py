import requests
from django.conf import settings


def send_otp(mobile, otp):
    """
    Send OTP via Textbelt API.
    """
    # URL для отправки SMS через Textbelt
    base_url = "https://textbelt.com/text"

    # Текст сообщения
    message_text = f"🔐 Ваш код для подтверждения: {otp}\n\n" \
                   f"Этот код был отправлен вам от Дуйшобаев Ислам.\n\n" \
                   f"⏳ Пожалуйста, введите его в течение 10 минут для завершения регистрации."

    payload = {
        "phone": mobile,  # Номер телефона получателя
        "message": message_text,  # Текст сообщения
        "key": settings.TEXTBELT_API_KEY,  # Ваш API-ключ для Textbelt
    }

    # Отправка POST запроса на Textbelt API
    response = requests.post(base_url, data=payload)

    # Проверка ответа
    if response.status_code == 200:
        result = response.json()
        if result.get('success'):
            return True
        else:
            return False
    else:
        return False
