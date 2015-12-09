from boto.s3.connection import S3Connection
 
AWS_KEY = 'KEY'
AWS_SECRET = 'SECRET_KEY'
aws_connection = S3Connection(AWS_KEY, AWS_SECRET)
bucket = aws_connection.get_bucket('bucket_name')
for file_key in bucket.list():
    print file_key.name