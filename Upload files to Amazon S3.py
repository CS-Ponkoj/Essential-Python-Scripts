# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 00:18:26 2021

@author: cspon
"""

import boto3
from boto3.s3.transfer import TransferConfig
import boto3.s3.transfer as s3transfer
import botocore
import glob


GB = 1024 ** 3
config = TransferConfig(multipart_threshold=5 * GB, max_concurrency=200)

image_folder = 'folder of the files/' #put the foldet path
bucket = 'bucketname'                 #put the bucket name


#put access  key id, secret access key and region name
s3_resource = boto3.resource('s3', aws_access_key_id='*******************',
                             aws_secret_access_key='**********************', region_name='region_name')
botocore_config = botocore.config.Config(max_pool_connections=20)
s3client = boto3.client('s3', aws_access_key_id='*******************',
                        aws_secret_access_key='************************', region_name='region_name',
                        config=botocore_config)

transfer_config = s3transfer.TransferConfig(
    use_threads=True,
    max_concurrency=20,
)

files_in_dir = []
files_in_dir += glob.glob(image_folder + '*.jpg')

# how many files to upload at once
n = 100

chunks = [files_in_dir[i * n:(i + 1) * n] for i in range((len(files_in_dir) + n - 1) // n)]

index = 1
for files_to_upload_list in chunks:
    s3t = s3transfer.create_transfer_manager(s3client, transfer_config)
    for f in files_to_upload_list:
        f = f.replace('foler path', '') #put the folder path
        file_name = image_folder + f
        key_name = f

        s3t.upload(
            file_name, bucket, key_name, extra_args={'ACL': 'public-read', 'ContentType': 'image/jpg'}
        )

    s3t.shutdown()  # wait for all the upload tasks to finish
    del s3t

    print(f'uploaded {n * index} images')
    index += 1
