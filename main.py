import streamlit as st
from app.encryption import encrypt_video, decrypt_video
from app.steganography import embed_secret_in_video, extract_secret_from_video
import os

st.title("Video Steganography App")
st.sidebar.header("Actions")
action = st.sidebar.radio(
    "Choose an action",
    [
        "Embed Secret Video", 
        "Extract Secret Video", 
        "Encrypt Video", 
        "Decrypt Video", 
        "Embed & Decrypt Workflow"
    ]
)

# Directories
DATA_DIR = "data/"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def download_file(file_path, label):
    """Generate a download link for a file."""
    with open(file_path, "rb") as f:
        data = f.read()
    st.download_button(
        label=f"Download {label}",
        data=data,
        file_name=os.path.basename(file_path),
        mime="video/mp4"
    )

if action == "Embed Secret Video":
    st.header("Embed Secret Video into Cover Video")
    cover_video = st.file_uploader("Upload Cover Video", type=["mp4", "avi", "mkv"])
    secret_video = st.file_uploader("Upload Secret Video", type=["mp4", "avi", "mkv"])
    password = st.text_input("Enter Password", type="password")
    if st.button("Embed"):
        if cover_video and secret_video and password:
            cover_path = os.path.join(DATA_DIR, cover_video.name)
            secret_path = os.path.join(DATA_DIR, secret_video.name)
            encrypted_path = os.path.join(DATA_DIR, "encrypted_secret.mp4")
            output_path = os.path.join(DATA_DIR, "output_video.mp4")

            with open(cover_path, "wb") as f:
                f.write(cover_video.read())
            with open(secret_path, "wb") as f:
                f.write(secret_video.read())

            with st.spinner("Embedding secret video..."):
                encrypt_video(secret_path, password, encrypted_path)
                embed_secret_in_video(cover_path, encrypted_path, output_path)

            st.success("Secret video embedded successfully!")
            st.video(output_path)
            download_file(output_path, "Embedded Video")

elif action == "Extract Secret Video":
    st.header("Extract Secret Video from Embedded Video")
    cover_video = st.file_uploader("Upload Embedded Video", type=["mp4", "avi", "mkv"])
    password = st.text_input("Enter Password", type="password")
    if st.button("Extract"):
        if cover_video and password:
            cover_path = os.path.join(DATA_DIR, cover_video.name)
            encrypted_path = os.path.join(DATA_DIR, "extracted_encrypted.mp4")
            decrypted_path = os.path.join(DATA_DIR, "decrypted_secret.mp4")

            with open(cover_path, "wb") as f:
                f.write(cover_video.read())

            with st.spinner("Extracting secret video..."):
                extract_secret_from_video(cover_path, encrypted_path)
                decrypt_video(encrypted_path, password, decrypted_path)

            st.success("Secret video extracted and decrypted successfully!")
            st.video(decrypted_path)
            download_file(decrypted_path, "Decrypted Video")

elif action == "Encrypt Video":
    st.header("Encrypt a Video")
    video = st.file_uploader("Upload Video to Encrypt", type=["mp4", "avi", "mkv"])
    password = st.text_input("Enter Password", type="password")
    if st.button("Encrypt"):
        if video and password:
            video_path = os.path.join(DATA_DIR, video.name)
            encrypted_path = os.path.join(DATA_DIR, "encrypted_video.mp4")
            
            with open(video_path, "wb") as f:
                f.write(video.read())

            with st.spinner("Encrypting video..."):
                encrypt_video(video_path, password, encrypted_path)

            st.success("Video encrypted successfully!")
            download_file(encrypted_path, "Encrypted Video")

elif action == "Decrypt Video":
    st.header("Decrypt an Encrypted Video")
    encrypted_video = st.file_uploader("Upload Encrypted Video", type=["mp4", "avi", "mkv"])
    password = st.text_input("Enter Password", type="password")
    if st.button("Decrypt"):
        if encrypted_video and password:
            encrypted_path = os.path.join(DATA_DIR, encrypted_video.name)
            decrypted_path = os.path.join(DATA_DIR, "decrypted_video.mp4")

            with open(encrypted_path, "wb") as f:
                f.write(encrypted_video.read())

            with st.spinner("Decrypting video..."):
                decrypt_video(encrypted_path, password, decrypted_path)

            st.success("Video decrypted successfully!")
            st.video(decrypted_path)
            download_file(decrypted_path, "Decrypted Video")

elif action == "Embed & Decrypt Workflow":
    st.header("Embed and Decrypt Secret Video")
    
    # Step 1: Embed Secret Video
    st.subheader("Step 1: Embed Secret Video")
    cover_video = st.file_uploader("Upload Cover Video", type=["mp4", "avi", "mkv"], key="cover")
    secret_video = st.file_uploader("Upload Secret Video", type=["mp4", "avi", "mkv"], key="secret")
    embed_password = st.text_input("Enter Password for Embedding", type="password", key="embed_pass")
    embed_button = st.button("Embed Secret Video")

    if embed_button and cover_video and secret_video and embed_password:
        cover_path = os.path.join(DATA_DIR, cover_video.name)
        secret_path = os.path.join(DATA_DIR, secret_video.name)
        encrypted_path = os.path.join(DATA_DIR, "encrypted_secret.mp4")
        embedded_video_path = os.path.join(DATA_DIR, "embedded_video.mp4")

        with open(cover_path, "wb") as f:
            f.write(cover_video.read())
        with open(secret_path, "wb") as f:
            f.write(secret_video.read())

        with st.spinner("Embedding secret video..."):
            encrypt_video(secret_path, embed_password, encrypted_path)
            embed_secret_in_video(cover_path, encrypted_path, embedded_video_path)

        st.success("Secret video embedded successfully!")
        st.video(embedded_video_path)
        download_file(embedded_video_path, "Embedded Video")

    # Step 2: Decrypt Extracted Video
    st.subheader("Step 2: Decrypt Extracted Secret Video")
    embedded_video = st.file_uploader("Upload Embedded Video", type=["mp4", "avi", "mkv"], key="embedded")
    decrypt_password = st.text_input("Enter Password for Decrypting", type="password", key="decrypt_pass")
    decrypt_button = st.button("Extract & Decrypt Secret Video")

    if decrypt_button and embedded_video and decrypt_password:
        embedded_path = os.path.join(DATA_DIR, embedded_video.name)
        extracted_encrypted_path = os.path.join(DATA_DIR, "extracted_encrypted.mp4")
        decrypted_secret_path = os.path.join(DATA_DIR, "decrypted_secret.mp4")

        with open(embedded_path, "wb") as f:
            f.write(embedded_video.read())

        with st.spinner("Extracting and decrypting secret video..."):
            extract_secret_from_video(embedded_path, extracted_encrypted_path)
            decrypt_video(extracted_encrypted_path, decrypt_password, decrypted_secret_path)

        st.success("Secret video extracted and decrypted successfully!")
        st.video(decrypted_secret_path)
        download_file(decrypted_secret_path, "Decrypted Secret Video")
