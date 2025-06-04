# upload_toS3_bucket.py
import boto3, os

s3 = boto3.client('s3')
bucket = "eagleeye-input"
folder = "/home/ubuntu/Object-detection-in-kubernetes/images/"

for filename in os.listdir(folder):
    if filename.lower().endswith(('.jpg', '.png', '.jpeg')):
        local_path = os.path.join(folder, filename)
        s3.upload_file(local_path, bucket, f"input-images/{filename}")
        print(f"✅ Uploaded {filename} to S3")
