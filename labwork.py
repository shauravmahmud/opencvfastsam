import streamlit as st
import cv2
import numpy as np

def brighten_image(image, amount):
    img_bright = cv2.convertScaleAbs(image, beta=amount)
    return img_bright

def blur_image(image, amount):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert image to RGB
    blur_img = cv2.GaussianBlur(img, (11, 11), amount)
    return blur_img

def enhance_details(img):
    hdr = cv2.detailEnhance(img, sigma_s=12, sigma_r=0.15)
    return hdr

def main():
    st.title("Image Processing App")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        file_bytes = uploaded_file.getvalue()
        image = cv2.imdecode(np.frombuffer(file_bytes, np.uint8), -1)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Process Image"):
            # do some cool image processing stuff
            processed_img = enhance_details(image)
            processed_img = brighten_image(processed_img, amount=25)
            processed_img = blur_image(processed_img, amount=0.2)
            
            st.image(processed_img, caption="Processed Image", use_column_width=True)

if __name__ == "__main__":
    main()
