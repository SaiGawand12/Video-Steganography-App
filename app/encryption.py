from cryptography.fernet import Fernet

def generate_key(password: str) -> Fernet:
    return Fernet(Fernet.generate_key())

def encrypt_video(video_path: str, password: str, output_path: str) -> str:
    key = generate_key(password)

    with open(video_path, "rb") as f:
        video_data = f.read()

    encrypted_data = key.encrypt(video_data)

    with open(output_path, "wb") as f:
        f.write(encrypted_data)

    return output_path

def decrypt_video(encrypted_path: str, password: str, output_path: str) -> str:
    key = generate_key(password)

    with open(encrypted_path, "rb") as f:
        encrypted_data = f.read()

    video_data = key.decrypt(encrypted_data)

    with open(output_path, "wb") as f:
        f.write(video_data)

    return output_path