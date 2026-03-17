# utils/qr_generator.py
import qrcode
import os

def generate_qr(ticket_id: str, url: str) -> str:
    os.makedirs("static/qrcodes", exist_ok=True)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4
    )
    qr.add_data(url)
    qr.make(fit=True)
    img  = qr.make_image(fill_color="black", back_color="white")
    path = f"static/qrcodes/{ticket_id}.png"
    img.save(path)
    return path
