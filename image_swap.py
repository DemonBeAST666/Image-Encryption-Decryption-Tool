import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
import random
import os

def swap_pixels(image, reverse=False, key=42):
    random.seed(key)
    h, w, c = image.shape
    swapped_image = image.copy()
    pixel_indices = [(i, j) for i in range(h) for j in range(w)]
    random.shuffle(pixel_indices)
    
    if reverse:
        pixel_indices.reverse()
    
    for idx in range(0, len(pixel_indices) - 1, 2):
        (x1, y1), (x2, y2) = pixel_indices[idx], pixel_indices[idx + 1]
        swapped_image[x1, y1], swapped_image[x2, y2] = swapped_image[x2, y2].copy(), swapped_image[x1, y1].copy()
    
    return swapped_image

def encrypt_image(image_path, output_path):
    ext = image_path.split('.')[-1]                                                                # Maintain original format
    base_name = os.path.basename(image_path)
    output_path = f"C:/py_img_purpose/encrypt_{base_name}"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)                                       # Ensure directory exists
    
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if image is None:
        print("Error: Unable to read image.")
        return
    
    encrypted_image = swap_pixels(image, key=42)
    success = cv2.imwrite(output_path, encrypted_image)
    if success:
        print(f"Encrypted image saved as {output_path}")
    else:
        print("Error: Failed to save encrypted image.")

def decrypt_image(image_path, output_path):
    ext = image_path.split('.')[-1]                                                                  # Maintain original format
    base_name = os.path.basename(image_path).replace("encrypt_", "")
    output_path = f"C:/py_img_purpose/decrypt_{base_name}"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)                                         # Ensure directory exists
    
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if image is None:
        print("Error: Unable to read image.")
        return
    
    decrypted_image = swap_pixels(image, reverse=True, key=42)
    success = cv2.imwrite(output_path, decrypted_image)
    if success:
        print(f"Decrypted image saved as {output_path}")
    else:
        print("Error: Failed to save decrypted image.")

if __name__ == "__main__":
    root = tk.Tk()
    root.lift()
    root.attributes('-topmost', True)
    root.withdraw()
    
    while True:
        action = input("What do you want to do? (encrypt/decrypt/exit): ").strip().lower()
        
        if action == "encrypt":
            input("Press Enter to pick an image...")
            image_path = filedialog.askopenfilename(title="Select Image")
            if not image_path:
                print("No image selected. Exiting...")
                exit()
            encrypt_image(image_path, "")
        
        elif action == "decrypt":
            encrypted_path = filedialog.askopenfilename(title="Select Encrypted Image", initialdir="C:/py_img_purpose")
            if not encrypted_path:
                print("No encrypted image selected. Exiting...")
                exit()
            decrypt_image(encrypted_path, "")
        
        elif action == "exit":
            print("Exiting program...")
            break
        
        else:
            print("Invalid choice. Please enter 'encrypt', 'decrypt', or 'exit'.")
