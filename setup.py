from setuptools import setup, find_packages
import os

# Read the contents of your README file
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="blob-your-face",
    version="0.1.1",
    author="crapthings",
    author_email="crapthings@gmail.com",
    description="A tool to detect faces in images and apply a blob effect",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/crapthings/py-blob-your-face",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "blob_your_face": ["yolov8n-face.pt"],
    },
    install_requires=[
        "opencv-python",
        "numpy",
        "ultralytics",
    ],
    entry_points={
        "console_scripts": [
            "blob_your_face=blob_your_face.main:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires='>=3.6',
    keywords='face detection, image processing, blob effect',
)