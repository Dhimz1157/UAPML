Gender Classification App

This project is a Streamlit-based application that allows users to classify gender from images. Users can either upload an image or capture one using their camera. The application supports two pre-trained models: ResNet50V2 and VGG16.

Installation Guide

Follow these steps to set up and run the application on your local machine:

Prerequisites

Python 3.7 or later

pip package manager

Internet connection to download required packages and models

Installation Steps

Install PDM (Python Dependency Manager):

(Invoke-WebRequest -Uri https://pdm-project.org/install-pdm.py -UseBasicParsing).Content | python -

Initialize a PDM project:

pdm init

Create a virtual environment:

python -m venv myenv

Activate the virtual environment:

On Windows:

myenv\scripts\activate

On MacOS/Linux:

source myenv/bin/activate

Install required packages:

pdm add tensorflow
pdm add numpy

Run the application:

pdm run streamlit run app.py

Dataset

The application uses a gender classification dataset for training the models. The dataset includes labeled images of males and females.

Pre-trained Models

The application supports the following pre-trained models:

ResNet50V2: A ResNet-based model optimized for gender classification.

VGG16: A VGG-based model optimized for gender classification.

Download Models

Download the pre-trained models and place them in the same directory as app.py:

ResNet50V2 Model

VGG16 Model

(Links to the models will be provided here)

Usage

Open the application in your browser using the provided URL from the Streamlit terminal output.

Choose one of the two options:

Take a photo: Use your camera to capture an image.

Upload an image: Upload an image file from your device.

Select the model (ResNet50V2 or VGG16) for prediction.

Click the "Predict" button to classify the gender.

View the results, including the predicted gender and confidence level.

Contributing

Contributions are welcome! Please create a pull request for any enhancements or bug fixes.

License

This project is licensed under the MIT License. See the LICENSE file for details.
