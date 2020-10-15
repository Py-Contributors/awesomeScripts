import os
import boto3

root_dir = os.getcwd()
S3_ACCESS_KEY_ID = ""  # YOUR ACCESS KEY
S3_SECRET_ACCESS_KEY = ""  # YOUR SECRET ACCESS KEY
S3_BUCKET_NAME = ""  # BUCKET NAME ON S3
STARTING_DIRECTORY = ""  # DIRECTORY ON S3 FROM WHERE YOU WANT TO RECURSIVELY DOWNLOAD THE DATA
# If you want to download the files with specific file extension then mention it as a list in the below variable.
# Otherwise all of the files will be downloaded. Ex- ['.csv', '.png']
FILE_EXTENSION = []


def download_dir(s3client, bucket, resource, dist, root_dir):
    paginator = s3client.get_paginator('list_objects')
    for result in paginator.paginate(Bucket=bucket, Delimiter='/', Prefix=dist):
        if result.get('CommonPrefixes') is not None:
            for subdir in result.get('CommonPrefixes'):
                download_dir(s3client, bucket, resource, subdir.get('Prefix'), root_dir)

        files = result.get('Contents', [])
        for file in files:
            if len(FILE_EXTENSION) == 0 or file.get('Key').endswith(tuple(FILE_EXTENSION)):
                local_pathname = os.path.join(root_dir, file.get('Key'))
                if not os.path.exists(os.path.dirname(local_pathname)):
                    os.makedirs(os.path.dirname(local_pathname))
                resource.meta.client.download_file(bucket, file.get('Key'), local_pathname)


if __name__ == '__main__':
    s3client = boto3.client('s3', aws_access_key_id=S3_ACCESS_KEY_ID , aws_secret_access_key=S3_SECRET_ACCESS_KEY)
    resource = boto3.resource('s3', aws_access_key_id=S3_ACCESS_KEY_ID , aws_secret_access_key=S3_SECRET_ACCESS_KEY)
    download_dir(s3client, S3_BUCKET_NAME, resource, STARTING_DIRECTORY, root_dir)
