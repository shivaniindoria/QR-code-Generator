import qrcode

def generate_qr_code(data, file_name="qrcode.png"):
    # Create an instance of the QRCode class
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(file_name)

if __name__ == "__main__":
    # Replace "Your Information Here" with the actual data you want in the QR code
    name = input("enter your name:")
    id = input("enter your id:")
    information= (f"my name is {name} employee of abc company and my id is{id}")
    # Generate the QR code
    generate_qr_code(information)
