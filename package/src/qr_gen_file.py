# qr code libraries
import qrcode
import qrcode.image.svg


def qr_code_generate():
    save_to_qr = input("Would you like to save this on a QR code? (Y/N): ")
    type(save_to_qr)

    def save_my_code():
        qrcode.make(save_to_qr)

    while save_to_qr.lower() == 'y':
        return save_my_code()
