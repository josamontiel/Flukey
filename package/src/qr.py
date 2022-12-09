import qrcode
import qrcode.image.svg
'''QR code generator which will be an option for users who generate a passcode'''


img = qrcode.make("Testing qr code generator")

type(img)

img.save("test_file.png")

## QR code png will auto generate and save 
