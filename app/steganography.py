import cv2
import numpy as np

def embed_secret_in_video(cover_path: str, secret_path: str, output_path: str):
    cover_cap = cv2.VideoCapture(cover_path)
    frame_width = int(cover_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cover_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cover_cap.get(cv2.CAP_PROP_FPS))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    with open(secret_path, "rb") as f:
        secret_data = f.read()

    secret_bits = ''.join(format(byte, '08b') for byte in secret_data)
    bit_idx = 0

    while True:
        ret, frame = cover_cap.read()
        if not ret:
            break

        for i in range(frame.shape[0]):
            for j in range(frame.shape[1]):
                if bit_idx < len(secret_bits):
                    frame[i, j, 0] = (frame[i, j, 0] & 0xFE) | int(secret_bits[bit_idx])
                    bit_idx += 1

        out.write(frame)

    cover_cap.release()
    out.release()

def extract_secret_from_video(cover_path: str, output_path: str):
    cap = cv2.VideoCapture(cover_path)
    secret_bits = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        for i in range(frame.shape[0]):
            for j in range(frame.shape[1]):
                secret_bits.append(frame[i, j, 0] & 1)

    secret_bytes = bytearray()
    for i in range(0, len(secret_bits), 8):
        byte = secret_bits[i:i+8]
        secret_bytes.append(int(''.join(map(str, byte)), 2))

    with open(output_path, "wb") as f:
        f.write(secret_bytes)

    cap.release()
    return output_path