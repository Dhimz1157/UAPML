
# Gender Classification App

## About Our App 🌟
<p align="justify">
This project is a Streamlit-based application that allows users to classify gender from images. Users can either upload an image or capture one using their camera. The application supports two pre-trained models: ResNet50V2 and VGG16.
</p>

---

## Installation Guide 🛠️

<p align="justify">
Follow these steps to set up and run the application on your local machine.
</p>

### Prerequisites

- **Python 3.7 or later**
- **pip package manager**
- **Internet connection** to download required packages and models

### Installation Steps

1. **Install PDM (Python Dependency Manager):**

   ```powershell
   (Invoke-WebRequest -Uri https://pdm-project.org/install-pdm.py -UseBasicParsing).Content | python -
   ```

2. **Initialize a PDM project:**

   ```bash
   pdm init
   ```

3. **Create a virtual environment:**

   ```bash
   python -m venv myenv
   ```

4. **Activate the virtual environment:**
   - On Windows:
     ```bash
     myenv\scriptsctivate
     ```
   - On MacOS/Linux:
     ```bash
     source myenv/bin/activate
     ```

5. **Install required packages:**
   ```bash
   pdm add tensorflow
   pdm add numpy
   ```

6. **Run the application:**
   ```bash
   pdm run streamlit run app.py
   ```

---

## Dataset 📂
<p align="justify">
The application uses a gender classification dataset for training the models. The dataset includes labeled images of males and females.
</p>

---

## Pre-trained Models 🧠

<p align="justify">
The application supports the following pre-trained models:
</p>

- **ResNet50V2**: A ResNet-based model optimized for gender classification.
- **VGG16**: A VGG-based model optimized for gender classification.

---

## Download Models 📥

<p align="justify">
Download the pre-trained models and place them in the same directory as `app.py`.
</p>

- [ResNet50V2 Model](#)
- [VGG16 Model](#)

*(Links to the models will be provided here)*

---

## Usage 🖥️

1. **Open the application in your browser** using the provided URL from the Streamlit terminal output.
2. **Choose one of the two options:**
   - **Take a photo**: Use your camera to capture an image.
   - **Upload an image**: Upload an image file from your device.
3. **Select the model** (ResNet50V2 or VGG16) for prediction.
4. **Click the "Predict" button** to classify the gender.
5. **View the results**, including the predicted gender and confidence level.

---

## Testing 🧪

To ensure all elements work as intended, follow these steps to test the application:

1. **Environment Setup:**
   Ensure the environment is set up correctly by following the installation guide above.

2. **Test Uploaded Image Prediction:**

   - Upload a sample image of a person.
   - Select the model (ResNet50V2 or VGG16).
   - Click "Predict" and verify the results.

3. **Test Camera Image Prediction:**

   - Use the "Take a photo" option to capture an image.
   - Select the model (ResNet50V2 or VGG16).
   - Click "Predict" and verify the results.

4. **Test Invalid Inputs:**

   - Try uploading a non-image file to ensure the application handles errors gracefully.
   - Test with low-resolution or unclear images to verify model behavior.

5. **UI Elements:**

   - Confirm that all buttons, radio options, and image displays are working as expected.
   - Ensure the model selection changes the underlying model used for predictions.

6. **Performance:**

   - Verify the application processes predictions within a reasonable time (<5 seconds).
   - Check the responsiveness of the application when switching between camera and upload modes.

---

## Contributing 🤝

<p align="justify">
Contributions are welcome! Please create a pull request for any enhancements or bug fixes.
</p>

---

## License 📜

<p align="justify">
This project is licensed under the MIT License. See the LICENSE file for details.
</p>
