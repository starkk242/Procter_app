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
        aws_access_key_id='ACCESS_KEYS',
        aws_secret_access_key='SECRET_ACCESS_KEYS'
    )

    bucket_name=get_bucket()


    file_name=enr+"/img.jpg"

    file_name1=enr+"/doc.jpg"

    send_file(file_name,img1_path)
    send_file(file_name1,img2_path)
