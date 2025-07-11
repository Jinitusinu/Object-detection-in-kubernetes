# Server-2
import boto3, os

s3 = boto3.client('s3')
bucket = "eagleeye-input"
local_folder = "/mnt/yolov5-data/input/"

os.makedirs(local_folder, exist_ok=True)

objects = s3.list_objects_v2(Bucket=bucket, Prefix="input-images/")
for obj in objects.get("Contents", []):
    key = obj["Key"]

    # Skip if it's a folder or empty key
    if key.endswith('/') or key == "input-images/":
        continue

    filename = os.path.basename(key)
    local_path = os.path.join(local_folder, filename)

    try:
        s3.download_file(bucket, key, local_path)
        print(f"⬇️ Downloaded {filename} to {local_path}")
    except Exception as e:
        print(f"❌ Failed to download {filename}: {e}")
