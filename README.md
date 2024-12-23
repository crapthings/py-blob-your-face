# Blob Your Face

A command-line tool to detect faces in images and apply a blob effect to them.

## Installation

```
pip install blob-your-face
```

## Usage

```
blob_your_face /path/to/input/folder [--color COLOR] [--shape SHAPE] [--pad PAD]
```

### Options:
- `--color`: Blob color in BGR format (e.g., '255,0,0' for blue). Default is white.
- `--shape`: Shape of the blob (circle, ellipse, rectangle, square). Default is circle.
- `--pad`: Padding size for the blob. Default is 0.

### Example:
```
blob_your_face ./inputs --color 255,0,0 --shape ellipse --pad 10
```

## Features

- Detects faces in images using YOLO v8.
- Applies a customizable blob effect to detected faces.
- Supports various blob shapes: circle, ellipse, rectangle, and square.
- Processes all supported image formats in the input directory.
- Creates a new output directory with a random suffix at the same level as the input directory.
- Preserves original filenames for processed images.

## Supported Image Formats

- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)

## Requirements

- Python 3.6+
- OpenCV
- NumPy
- Ultralytics YOLO
- Pillow

## Note

This tool requires the `yolov8n-face.pt` model file to be present in the working directory or specified path.
