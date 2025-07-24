# **Handwritten Digit Recognizer**
## **Project Description**
This project implements a simple yet effective web application for recognizing handwritten digits using a Convolutional Neural Network (CNN). The application is built with Streamlit, allowing users to draw a digit directly on a canvas, and then uses a pre-trained TensorFlow/Keras model to predict the drawn digit. It's an interactive demonstration of a basic machine learning model in action.

[Project Preview](https://www.linkedin.com/posts/arup-paul-963810194_deeplearning-machinelearning-computervision-activity-7326703486551625729-wIz3?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAC2utlsBN0vjeA-294JY4j4XIxX0_K8moz0)

## **Features**
- **Interactive Drawing Canvas:** Users can draw digits (0-9) directly in the web browser.
- **Real-time Prediction:** On button click, the drawn digit is processed and predicted by a CNN model.
- **Clear Output:** Displays the predicted digit and the confidence level of the prediction.
- **User-Friendly Interface:** Built with Streamlit for a simple and intuitive user experience.

## **How to Run**
Follow these steps to set up and run the Handwritten Digit Recognizer on your local machine.

### Prerequisites
- Python 3.7+
- pip (Python package installer)

### 1. Download the Project
You can download this project by cloning its Git repository. If you don't have Git installed, you can also download the project as a ZIP file from the repository's page (if available).

```
git clone <repository_url>
cd handwritten-digit-recognizer # Replace with your project directory name
```

If you're creating the files manually, save the provided Python code as app.py and ensure you have the mnist_cnn.keras model file in the same directory.

### 2. Set up Virtual Environment and Install Dependencies
It is highly recommended to use a virtual environment to manage project dependencies.

### 1. Create a virtual environment:
    python -m venv venv

### 2. Activate the virtual environment:
- **On Windows:**
     ```
     .\venv\Scripts\activate
     ```

- **On macOS/Linux:**
    ```
    source venv/bin/activate
    ```
- **Install dependencies from requirements.txt:**
    ```
    pip install -r requirements.txt
    ```

### 3. Run the Streamlit Application
Once all dependencies are installed and the model file is in place, run the Streamlit application from your terminal:

    streamlit run app.py

This command will open the application in your default web browser. If it doesn't open automatically, Streamlit will provide a local URL (e.g., http://localhost:8501) that you can copy and paste into your browser.

## Usage
- **Draw:** Use your mouse or touchscreen to draw a single digit (0-9) within the white canvas area. Try to make the digit clear and centered.
- **Predict:** Click the "🔍 Predict" button below the canvas.
- **View Result:** The predicted digit and its confidence score will be displayed below the button.
- **Clear:** To draw a new digit, simply draw over the existing one. The canvas automatically updates.

## Model Details
The application uses a Convolutional Neural Network (CNN) trained on the MNIST dataset. The MNIST dataset consists of 28x28 pixel grayscale images of handwritten digits. The CNN architecture is designed to effectively extract features from these images and classify them into one of 10 categories (0-9).

## Dependencies
- ```streamlit```
- ```streamlit-drawable-canvas```
- ```tensorflow```
- ```numpy```
- ```Pillow (PIL)```

## License
This project is open-source and available under the MIT License.