### QR Code Generator
QR generator application in Python using the QRCode library and Streamlit to create a web application.
## Technologies used
- Code Editor: Visual Studio Code;
- Programming Language: Python;
- Python Libraries:
	- QRCODE: Library used to generate the QR Codes
	- streamlit: To create the webpage

## Functionality
The structure consists of a web application in which we insert a web link and it returns a QR code that we can download.
##Installation and Setup
Follow these steps to install and set up the project on your machine:

#1.- Clone this repository
**Download the source code using git clone or by downloading the ZIP file from GitHub:
	git clone https://github.com/your_username/your_repository.git
	cd your_repository

#2.- Set up a virtual environment (optional but recommended)
**It's recommended to use a virtual environment to avoid dependency conflicts. You can set it up with the following commands:

	python -m venv venv
	source venv/bin/activate      # On Linux/Mac
	venv\Scripts\activate         # On Windows

#3.- Install the required dependencies
**To run the project, you'll need to install the following Python libraries:

- streamlit: For building the web interface.
- qrcode: For generating QR codes.

You have three options to install the dependencies:

**Option 1: Install all dependencies at once from requirements.txt**
If you have a requirements.txt file, use the following command to install all dependencies:

	pip install -r requirements.txt

**Option 2: Install all dependencies manually at once**
Use the following command to install both libraries:

	pip install streamlit qrcode

**Option 3: Install dependencies manually**
Alternatively, you can install each library individually:

	pip install streamlit
	pip install qrcode

Any of these methods will ensure the necessary libraries are installed.

#4.- Create the required folders
**Ensure that the necessary folders exist in your project directory:

	mkdir -p qr_codes images

#5.- Add the icon (qricon.png)
**Place an image file named qricon.png in the images folder. This will be used as the icon in the application. If you don’t have an image, you can either remove or modify this functionality in the code.

#6.-Run the application
**Start the Streamlit server to view the application:

	streamlit run your_script_name.py

Replace your_script_name.py with the name of the file containing the code. In this case is: QRgen.py

	streamlit run QRgen.py
