# setup.py

from setuptools import setup, find_packages

setup(
    name="blob_your_face",
    version="0.1",
    packages=find_packages(),
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
    include_package_data=True,
    package_data={
        "blob_your_face": ["yolov8n-face.pt"],
    },
)