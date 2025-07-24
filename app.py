import streamlit as st
from streamlit_drawable_canvas import st_canvas
import numpy as np
import tensorflow as tf
from PIL import Image, ImageOps

# Load model
model = tf.keras.models.load_model("mnist_cnn.keras")

st.set_page_config(page_title="Handwritten Digit Recognizer", layout="centered")

st.title("✍️ Draw a Digit (0-9)")
st.markdown("Draw a digit below and click **Predict** to identify it.")

# Create canvas component
canvas_result = st_canvas(
    fill_color="white",  # background color
    stroke_width=15,
    stroke_color="black",
    background_color="white",
    height=280,
    width=280,
    drawing_mode="freedraw",
    key="canvas",
)

if canvas_result.image_data is not None:
    # Convert image to PIL
    img = Image.fromarray((canvas_result.image_data).astype("uint8"))
    img = img.convert('L')  # Grayscale
    img = ImageOps.invert(img)  # Invert to match MNIST style (white digit on black)
    img = img.resize((28, 28))
    img_arr = np.array(img).astype('float32') / 255.0
    img_arr = img_arr.reshape(1, 28, 28, 1)

    if st.button("🔍 Predict"):
        prediction = model.predict(img_arr)
        digit = np.argmax(prediction)
        confidence = np.max(prediction)
        st.markdown(f"### Prediction: `{digit}`")
else:
    st.warning("Please draw a digit in the canvas.")
