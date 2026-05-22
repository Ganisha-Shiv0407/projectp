from flask import Flask, render_template, send_file
import io
import os
import qrcode

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# NEW ROUTE: Generates the QR code dynamically
@app.route('/get_qr')
def get_qr():
    # Change this URL to your real live link once you deploy your app!
    website_url = "https://your-ecocity-dashboard.onrender.com" 
    
    # Configure the QR code properties
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(website_url)
    qr.make(fit=True)

    # Stylize the QR Code to perfectly match the EcoCity UI theme
    # Dark Background: #0b0f19 | Vibrant Teal Pixels: #20B2AA
    img = qr.make_image(fill_color="#20B2AA", back_color="#0b0f19")
    
    # Compress and save image into a fluid memory byte stream
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    
    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    # Dynamic port allocation optimized for Render deployment engines
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
