# पहले यह लाइब्रेरी इंस्टॉल कर लो:
# pip install qrcode[pil]

import qrcode

# जो टेक्स्ट या लिंक QR में डालना है
data = "NAME = KAMAL KUMAR " \
"MOB. = 8955494801" \
"ADD. = VILLAGE - KANSAR,NOHAR, " \
"PIN. = 335523" \
"" \

# QR Code बनाना
qr = qrcode.QRCode(
    version=1,  # QR Code का साइज (1 से 40 तक)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
    box_size=10,  # हर बॉक्स का साइज
    border=4,     # बॉर्डर चौड़ाई
)

qr.add_data(data)
qr.make(fit=True)

# QR Code इमेज बनाना
img = qr.make_image(fill_color="black", back_color="white")

# फाइल सेव करना
img.save("my_qr.png")

print("QR Code बन गया: my_qr.png")
