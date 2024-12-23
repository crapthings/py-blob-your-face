import cv2
import numpy as np
from ultralytics import YOLO
import os
import argparse
import random
import string

def create_mask(shape, center, size, mask_type='circle'):
    mask = np.zeros(shape[:2], dtype=np.uint8)
    if mask_type == 'circle':
        cv2.circle(mask, center, size[0], (255, 255, 255), -1)
    elif mask_type == 'ellipse':
        cv2.ellipse(mask, center, size, 0, 0, 360, (255, 255, 255), -1)
    elif mask_type in ['rectangle', 'square']:
        x, y = center
        w, h = size
        cv2.rectangle(mask, (x - w//2, y - h//2), (x + w//2, y + h//2), (255, 255, 255), -1)
    mask = cv2.GaussianBlur(mask, (51, 51), 0)
    return mask

def apply_blob_effect(image, face, color, shape, pad):
    x, y, w, h = face
    center = (x + w // 2, y + h // 2)
    size = (max(w, h) // 2 + pad, max(w, h) // 2 + pad)
    if shape == 'square':
        size = (size[0], size[0])

    blob_mask = create_mask(image.shape, center, size, shape)
    
    colored_image = np.full(image.shape, color, dtype=np.uint8)
    result = image.copy()
    result = np.where(blob_mask[:, :, np.newaxis] > 0, colored_image, result)
    
    return result

def detect_and_blob_faces(image_path, output_path, color, shape, pad):
    # Load YOLO model
    model = YOLO('yolov8n-face.pt')

    # Read the image
    image = cv2.imread(image_path)
    
    if image is None:
        print(f"Error: Unable to read image {image_path}")
        return

    # Perform face detection
    results = model(image)
    
    # Process each detected face
    for result in results:
        boxes = result.boxes.xyxy.cpu().numpy().astype(int)
        for box in boxes:
            x1, y1, x2, y2 = box
            face = (x1, y1, x2 - x1, y2 - y1)
            image = apply_blob_effect(image, face, color, shape, pad)
    
    # Save the result
    cv2.imwrite(output_path, image)
    print(f"Processed image saved to {output_path}")

def process_directory(input_dir, output_dir, color, shape, pad):
    supported_formats = ['.jpg', '.jpeg', '.png', '.bmp']
    
    for filename in os.listdir(input_dir):
        if any(filename.lower().endswith(ext) for ext in supported_formats):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            detect_and_blob_faces(input_path, output_path, color, shape, pad)

def main():
    parser = argparse.ArgumentParser(description="Apply blob effect to faces in images.")
    parser.add_argument("input_dir", help="Input directory containing images")
    parser.add_argument("--color", default="255,255,255", help="Blob color in BGR format (e.g., '255,0,0' for blue)")
    parser.add_argument("--shape", choices=['circle', 'ellipse', 'rectangle', 'square'], default='circle', help="Shape of the blob")
    parser.add_argument("--pad", type=int, default=0, help="Padding size for the blob")
    args = parser.parse_args()

    input_dir = os.path.abspath(args.input_dir)
    parent_dir = os.path.dirname(input_dir)
    base_name = os.path.basename(input_dir)
    random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=3))
    output_dir = os.path.join(parent_dir, f"{base_name}_{random_suffix}")
    os.makedirs(output_dir, exist_ok=True)

    color = tuple(map(int, args.color.split(',')))
    
    process_directory(input_dir, output_dir, color, args.shape, args.pad)

if __name__ == "__main__":
    main()