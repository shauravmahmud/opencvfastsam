import streamlit as st
import cv2
import numpy as np

def main():
    st.title("Image Upload App")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        file_bytes = uploaded_file.read()
        nparr = np.frombuffer(file_bytes, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        st.image(image, caption="Uploaded Image", use_column_width=True)

if __name__ == "__main__":
    main()
