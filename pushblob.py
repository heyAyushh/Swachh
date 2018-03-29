# Create a file in Documents to test the upload and download.
import sys
from azure.storage.blob import BlockBlobService

block_blob_service = BlockBlobService(account_name='', account_key='')
# Upload the created file, use local_file_name for the blob name
""" block_blob_service.create_blob_from_path(container_name, local_file_name, full_path_to_file) """
block_blob_service.create_blob_from_path
('container_name', sys.argv[1], sys.argv[2])

print("hogya upload")
