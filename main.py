import os.path
import boto3
import cv2
import credentials
import os

output_dir = './data'
output_dir_imgs = os.path.join(output_dir, 'imgs')
output_dir_anns = os.path.join(output_dir, 'anns')

# Create AWS Reko Client
reko_client = boto3.client('rekognition',
                           aws_access_key_id=credentials.access_key,
                           aws_secret_access_key=credentials.secret_key,
                           region_name='ap-south-1')

# Load the video
cap = cv2.VideoCapture('C://Users//tavha//PycharmProjects//pythonProject//store.mp4')

frame_nmr = -1

# Read frames
while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame_nmr += 1
    H, W, _ = frame.shape

    # Convert frame to jpg
    _, buffer = cv2.imencode('.jpg', frame)

    # Convert buffer to bytes
    image_bytes = buffer.tobytes()

    # Detect objects
    response = reko_client.detect_labels(Image={'Bytes': image_bytes}, MinConfidence=50)

    with open(os.path.join(output_dir_anns, 'frame_{}.txt'.format(str(frame_nmr).zfill(6))), 'w') as f:
        for label in response['Labels']:
            for instance in label.get('Instances', []):
                bbox = instance['BoundingBox']
                x1 = bbox['Left'] * W
                y1 = bbox['Top'] * H
                width = bbox['Width'] * W
                height = bbox['Height'] * H
                print(label['Name'], x1, y1, width, height)
                # Write detections
                f.write('{} {} {} {} {}\n'.format(label['Name'], x1 + width / 2, y1 + height / 2, width, height))

    cv2.imwrite(os.path.join(output_dir_imgs, 'frame_{}.jpg'.format(str(frame_nmr).zfill(6))), frame)

cap.release()
cv2.destroyAllWindows()
