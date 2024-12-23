import qrcode
import streamlit as st

#Initial configuration
st.set_page_config(page_title="My QR Code Generator", page_icon=None, layout="centered")

#Path of the file to save the QR Code
filename = "qr_codes/qr_code.png"

#Title and icon image
st.image("images/qricon.png", use_container_width=True)
st.title("QR Code Generator")

# Function to generate the QR code
def generate_qr_code(url, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

#Entering the URL
url = st.text_input("Enter the URL")

#Button to generate the QR Code
if st.button("Generate QR Code"):
    generate_qr_code(url, filename)
    st.image(filename, use_column_width=True)
    with open(filename, "rb") as f:
        image_data = f.read()
    st.download_button(label="Download QR Code", data=image_data, file_name="qr_generated.png")
       



 

        