# server-2
import boto3, os

s3 = boto3.client('s3')
bucket = "eagleeye-output"
folder = "/mnt/yolov5-data/output/results/"

for filename in os.listdir(folder):
    if filename.lower().endswith(('.jpg', '.png', '.jpeg')):
        local_path = os.path.join(folder, filename)
        s3.upload_file(local_path, bucket, f"output-images/{filename}")
        print(f"✅ Uploaded {filename} to S3")
