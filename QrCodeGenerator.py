import qrcode
import image
qr=qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)
data="https://chatgpt.com/c/5b596375-b891-4616-9fa3-85499c888416"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save("test.png")
