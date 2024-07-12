import qrcode
import numpy as np

def generate_qr_matrix(url):
    # Generate QR code matrix
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=1,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    # Convert the QR code to a numpy array
    qr_matrix = np.array(qr.get_matrix(), dtype=int)
    return qr_matrix

def matrix_to_html(qr_matrix, url):
    # Generate HTML content from the QR matrix
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>QR Code Email</title>
    </head>
    <body style="font-family: Arial, sans-serif; background-color: #f4f4f4; margin: 0; padding: 0; text-align: center;">
        <div style="margin: 20px auto; padding: 20px; background-color: #fff; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); border-radius: 8px; max-width: 600px;">
            <h1>Your QR Code</h1>
            <p>Scan the QR code below to visit the link:</p>
            <div style="display: inline-block; line-height: 0; font-size: 0;">
    """

    cell_size = 10  # Size of each cell in the QR code
    for row in qr_matrix:
        html += '<div style="clear: both;">'
        for cell in row:
            color = '#000' if cell else '#fff'
            html += f'<div style="display: inline-block; width: {cell_size}px; height: {cell_size}px; background-color: {color};"></div>'
        html += '</div>'
    
    html += f"""
            </div>
            
        </div>
    </body>
    </html>
    """

    return html

# Example usage
url = input("Enter the URL you want to link to: ")
qr_matrix = generate_qr_matrix(url)
email_html = matrix_to_html(qr_matrix, url)
print(email_html)
