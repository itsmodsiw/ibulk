# modsiw's iBulk Image Converter

[![Python](https://img.shields.io/badge/Python-3.9-blue?style=flat-square&logo=python)](https://www.python.org/downloads/release/python-390/)
[![Flask](https://img.shields.io/badge/Flask-2.0.1-blue?style=flat-square&logo=flask)](https://flask.palletsprojects.com/)
[![Pillow](https://img.shields.io/badge/Pillow-8.3.1-blue?style=flat-square&logo=pypi)](https://pypi.org/project/Pillow/)
[![NumPy](https://img.shields.io/badge/NumPy-1.21.0-blue?style=flat-square&logo=numpy)](https://numpy.org/)
[![SciPy](https://img.shields.io/badge/SciPy-1.7.0-blue?style=flat-square&logo=scipy)](https://www.scipy.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.5.3-blue?style=flat-square&logo=opencv)](https://opencv.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.4.2-blue?style=flat-square&logo=python)](https://matplotlib.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.5.0-blue?style=flat-square&logo=tensorflow)](https://www.tensorflow.org/)
[![Keras](https://img.shields.io/badge/Keras-2.4.3-blue?style=flat-square&logo=keras)](https://keras.io/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-0.24.2-blue?style=flat-square&logo=scikit-learn)](https://scikit-learn.org/)
[![GIMP](https://img.shields.io/badge/GIMP-2.10.24-blue?style=flat-square&logo=gimp)](https://www.gimp.org/)
[![Inkscape](https://img.shields.io/badge/Inkscape-1.1-blue?style=flat-square&logo=inkscape)](https://inkscape.org/)

Welcome to modsiw's iBulk Image Converter! This web application is designed to make image conversion a breeze. It allows you to convert multiple images in bulk to different formats with ease and efficiency. Say goodbye to tedious manual conversions, irritating ads, annoying pop-ups, and spammy interfaces. With iBulk, you can save time and effort while enjoying a user-friendly, efficient, and ad-free experience.

## Table of Contents
- [Features](#features)
- [Installation and Usage](#installation-and-usage)
- [How to Use](#how-to-use)
- [Accessing the Application](#accessing-the-application)
- [Deploying to Heroku](#deploying-to-heroku)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Bulk Image Conversion**: Convert multiple images in one go, saving you time and effort.
- **Flexible Output Formats**: Convert images to different formats such as PNG, JPG, JPEG, and GIF.
- **Image Resizing**: Resize images by setting custom dimensions to meet your specific requirements.
- **User-Friendly Interface**: Enjoy a clean and intuitive interface that makes the conversion process smooth and hassle-free.
- **Ad-Free Experience**: Say goodbye to annoying ads and distractions while using iBulk.

## Installation and Usage
To use modsiw's iBulk Image Converter, follow the steps below:

```shell
# Clone the repository
git clone https://github.com/itsmodsiw/ibulk.git

# Navigate to the project directory
cd ibulk

# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate

# Install the required dependencies
pip install -r requirements.txt

# Start the Flask development server
flask run

```

## How to Use
Follow these steps to convert images using modsiw's iBulk Image Converter:

1. Open your web browser and navigate to `http://localhost:5000`.
2. Choose the images you want to convert by clicking the "Choose images" button and selecting multiple files. Supported formats are PNG, JPG, JPEG, and GIF.
3. Select the desired output format from the dropdown menu.
4. (Optional) If you want to resize the images, toggle the "Set Dimensions" switch and enter the desired width and height in pixels.
5. Click the "Convert" button to start the conversion process.
6. Your converted images will be downloaded as a ZIP file automatically.

## Accessing the Application
To access the iBulk Image Converter application:

1. Open your web browser.
2. Enter the URL `http://localhost:5000`.
3. The iBulk Image Converter interface will be displayed.

## Deploying to Heroku
To deploy the iBulk Image Converter application to Heroku, follow these steps:

1. Create a new Heroku app.
2. Set the necessary environment variables or config vars in Heroku:
   - `FLASK_APP=app.py`
   - `FLASK_ENV=production`
3. Deploy the application to Heroku using your preferred method (e.g., Heroku CLI, Git-based deployment).
4. Once deployed, access the application using the provided Heroku app URL.

## Contributing
Contributions to modsiw's iBulk Image Converter are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

---

Developed by [modsiw](https://twitter.com/itsmodsiw) with ❤️.

If you find iBulk Image Converter helpful, don't forget to give it a ⭐️!
```
