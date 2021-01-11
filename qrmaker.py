# This application makes qrcodes using the qrcode library
# using pip to install the library (pip install qrcode)

import qrcode # Import the qrcode library

# Data to embed in qrcode
data = 'Read more about qrcode library\n https://pypi.org/project/qrcode/'

qr = qrcode.QRCode(version=1, box_size=10, border=5) #Control the size of the image

qr.add_data(data) # add the data to the qrcode
qr.make(fit=True) 

img = qr.make_image(fill='red', back_color='white') #Create image
img.save('mycode.png', 'PNG') # Save the image as a .png file
