def upload_files(enr,img1_path,img2_path):
    import boto3
    #import os

    def get_bucket():
            for bucket in s3.buckets.all():
                    return (bucket.name)

    def send_file(file_name,file_dir):
            #s3.create_bucket(Bucket= bucket_name)
            s3.Object(bucket_name,file_name).upload_file(Filename=file_dir)

    s3 = boto3.resource(
        service_name='s3',
        endpoint_url = 'https://s3.eu-central-1.wasabisys.com',
        aws_access_key_id='7FMNYNLSLR5G6B2VT8U6',
        aws_secret_access_key='4rR9rzGah2tjnZHG5sCpMSm6vHzXDWVF7uUPKziw'
    )

    bucket_name=get_bucket()


    file_name=enr+"/img.jpg"

    file_name1=enr+"/doc.jpg"

    send_file(file_name,img1_path)
    send_file(file_name1,img2_path)