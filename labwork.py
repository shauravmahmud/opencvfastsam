import streamlit as st
import cv2
from PIL import Image
import numpy as np

def main():
    st.title("Image Upload App")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        file_bytes = uploaded_file.read()
        nparr = np.frombuffer(file_bytes, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Convert OpenCV image to PIL format
        pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        
        # Display the image using Streamlit
        st.image(pil_image, caption="Uploaded Image", use_column_width=True)

if __name__ == "__main__":
    main()
