# **Video Steganography App**

This is a **Streamlit-based web application** that allows users to securely hide a secret video inside a cover video using **video steganography techniques**. The app also provides functionality to **encrypt and decrypt videos** for added security.

---

## **Features**

1. **Embed Secret Video**
   - Hides a secret video inside a cover video with password protection.
   - Encrypts the secret video before embedding for double-layer security.

2. **Extract Secret Video**
   - Extracts the secret video from an embedded video.
   - Decrypts the extracted video using the same password.

3. **Encrypt Video**
   - Encrypts a video file using a password to protect its content.

4. **Decrypt Video**
   - Decrypts a previously encrypted video file using the correct password.

5. **Embed & Decrypt Workflow**
   - Combines embedding and decryption in a single workflow:
     - Embed a secret video into a cover video.
     - Extract and decrypt the secret video when needed.

6. **Downloadable Outputs**
   - After any operation, the output video can be downloaded directly.

7. **Loading Effects**
   - Provides a visual loading indicator to show progress during operations.

---

## **Tech Stack**

- **Programming Language**: Python
- **Framework**: Streamlit
- **Libraries**:
  - `os` for file handling.
  - `cv2` (OpenCV) for video processing.
  - Custom modules:
    - `encryption.py`: Handles video encryption and decryption.
    - `steganography.py`: Implements video steganography.

---

## **Installation**

Follow these steps to set up and run the app locally.

### 1. Clone the Repository

```bash
git clone https://github.com/SaiGawand12/Video-Steganography-App.git
cd Video-Steganography-App
```

### 2. Set Up a Virtual Environment

Create a virtual environment to manage dependencies.

```bash
python -m venv env
source env/bin/activate       # For Linux/Mac
env\Scripts\activate          # For Windows
```

### 3. Install Dependencies

Install the required libraries using `pip`.

```bash
pip install -r requirements.txt
```

### 4. Run the App

Start the Streamlit server.

```bash
streamlit run main.py
```

---

## **Usage**

1. Open the app in your browser (default URL: [http://localhost:8501](http://localhost:8501)).
2. Select an action from the sidebar:
   - **Embed Secret Video**
   - **Extract Secret Video**
   - **Encrypt Video**
   - **Decrypt Video**
   - **Embed & Decrypt Workflow**
3. Follow the prompts to upload videos, enter passwords, and perform operations.
4. Download the processed video once the operation completes.

---

## **File Structure**

```
video_steganography/
│
├── app/
│   ├── __init__.py          # Optional, for module initialization
│   ├── encryption.py        # Encryption and decryption utilities
│   ├── steganography.py     # Video embedding and extraction utilities
│
├── data/                    # Directory for input/output videos
│   ├── cover_video.mp4      # Example cover video
│   ├── secret_video.mp4     # Example secret video
│   └── output_video.mp4     # Embedded output video
│
├── main.py                  # Streamlit app entry point
├── requirements.txt         # Dependencies
├── README.md                # Documentation
└── venv/                    # Virtual environment directory (after setup)

```

---

## **Features in Detail**

### **1. Embed Secret Video**
- **Input**: A cover video, a secret video, and a password.
- **Process**:
  - Encrypts the secret video using the password.
  - Hides the encrypted secret video inside the cover video.
- **Output**: A new video file containing the embedded secret video.

### **2. Extract Secret Video**
- **Input**: An embedded video and the correct password.
- **Process**:
  - Extracts the encrypted secret video from the cover video.
  - Decrypts the secret video using the password.
- **Output**: The original secret video.

### **3. Encrypt Video**
- **Input**: A video file and a password.
- **Process**: Encrypts the video using the password.
- **Output**: A secure, encrypted video file.

### **4. Decrypt Video**
- **Input**: An encrypted video file and the correct password.
- **Process**: Decrypts the video.
- **Output**: The original video file.

### **5. Embed & Decrypt Workflow**
- **Embed**:
  - Encrypts and embeds a secret video into a cover video.
- **Decrypt**:
  - Extracts and decrypts the secret video from the embedded file.

---

## **Security Features**

- **Encryption**:
  - All secret videos are encrypted using a password before embedding.
  - The decryption process requires the same password used during encryption.
- **Steganography**:
  - Ensures the secret video is hidden without visibly altering the cover video.

---

## **Demo**

1. Select "Embed & Decrypt Video" from the sidebar.
2. Upload a cover video and a secret video.
3. Enter a password and click **Embed Secret Video**.
4. Download the embedded video.
5. Upload the embedded video, enter the password, and click **Extract & Decrypt Secret Video**.
6. Download the extracted secret video.

---

## **Troubleshooting**

1. **App Not Starting**:
   - Ensure all dependencies are installed (`pip install -r requirements.txt`).
   - Check if the virtual environment is activated.

2. **Slow Performance**:
   - Use lower-resolution videos for faster processing.
   - Ensure sufficient system resources are available.

3. **Incorrect Password**:
   - Make sure the same password is used for encryption and decryption.

---

## **Future Enhancements**

1. **Add Audio Steganography**:
   - Extend functionality to hide audio files within videos.
2. **Performance Optimization**:
   - Implement GPU acceleration for faster processing.
3. **Cloud Deployment**:
   - Deploy the app to platforms like AWS, Azure, or Heroku for public access.

---

## **License**

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## **Contributing**

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request with detailed explanations.

---