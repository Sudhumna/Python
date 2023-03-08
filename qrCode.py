import qrcode as qr
img = qr.make("http://sudhumnaphuyal.com.np/")
img.save("mysite.png")