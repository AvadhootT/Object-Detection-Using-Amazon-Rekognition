# Object Detection Using Amazon Rekognition

This project aims to demonstrate the implementation of object detection using Amazon Rekognition, a deep learning-based image and video analysis service provided by Amazon Web Services (AWS). The script provided in this repository allows for the detection of various objects in a video using the Amazon Rekognition API.

## Project Overview

Video Processing: The script takes the video path as input and converts it into individual frames for subsequent analysis.

Frame Conversion: Each frame is then converted to the .jpg format, making it compatible with the object detection process.

Object Detection Logic: Using the Amazon Rekognition API, the script applies advanced object detection algorithms to the frames, enabling the identification of various objects within the video.

## Getting Started

To get started with this project, follow the steps below:

### Prerequisites

- Python 3.x
- AWS account with necessary permissions
- OpenCV (cv2) library
- Boto3 library

## Install the required libraries:

pip install opencv-python
pip install boto3

## Set up your AWS credentials 

Create your AWS_Access_Key and AWS_Security_Key from AWS Account .

And accordingly change the details in credentials.py file.

And while using the credentials in the main.py script do not forget to mention the region from where credentials are created.

In my case, I have created in Mumbai region and the code for this region is 'ap-south-1'.

## Run the main.py script:

main.py

In this script you can detect the objects in two ways:
1. By specifying the target class and accordingly iterating frame by frame.
2. And the way I have implemented, i.e detect all the objects which are present in every frame.

## Usage
Ensure that the target video file is located in the specified directory.
Adjust the target classes and other parameters in the script as needed.
Execute the script to perform object detection on the specified video file.
Check the data directory for the generated images and annotations.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or create a pull request.

Acknowledgements
This project was created as part of a learning exercise and for demonstration purposes.
Thanks to AWS for providing the Rekognition service and the open-source community for their valuable contributions to the libraries used in this project.
