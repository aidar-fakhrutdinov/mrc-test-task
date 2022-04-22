import boto3
from botocore.exceptions import ClientError
from robot.api.deco import keyword, library


@library
class BucketVerification:
    ROBOT_LIBRARY_SCOPE = 'SUITE'
    ROBOT_AUTO_KEYWORDS = False

    def __init__(self, aws_access_key_id: str, aws_secret_access_key: str, region_name: str):
        self.session = boto3.Session(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name
        )

    @keyword('Get Bucket List')
    def get_bucket_list(self):
        s3 = self.session.resource('s3')
        try:
            buckets = [bucket.name for bucket in s3.buckets.all()]
            return buckets
        except ClientError:
            return []

    @keyword('Verify Bucket Encryption')
    def verify_bucket_encryption(self, bucket: str):
        s3 = self.session.client('s3')
        try:
            encryption = s3.get_bucket_encryption(Bucket=bucket)
            rules = encryption['ServerSideEncryptionConfiguration']['Rules']
            return f"Bucket: {bucket}, Encryption: {rules}"
        except ClientError as e:
            if e.response['Error']['Code'] == 'ServerSideEncryptionConfigurationNotFoundError':
                return f"Bucket: {bucket}, no server-side encryption"
            else:
                return f"Invalid credentials"
