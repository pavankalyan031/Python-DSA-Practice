import qrcode 

url = input("Enter the URL: ").strip()
file_path= "C:\\Users\\vaira\\Downloads\\Python Practice-20260613T152743Z-3-001\\qr_code.png"

qr= qrcode.QRCode()
qr.add_data(url)

img= qr.make_image()
img.save(file_path)

print("QR Code is generated successfully!")