import boto3
from logging import getLogger, INFO

s3 = boto3.client('s3')
logger = getLogger(__name__)
logger.setLevel(INFO)


# s3-get-object
def get_object_from_bucket(bucket_name, object_name):
    try:
        return s3.get_object(Bucket=bucket_name, Key=object_name)
    except Exception as e:
        logger.error(
            f"Error while getting object from bucket {bucket_name} with key {object_name} : {e}")
        raise e


def put_object_into_bucket(bucket_name, object_name, data):
    try:
        return s3.put_object(Bucket=bucket_name, Key=object_name, Body=data)
    except Exception as e:
        logger.error(
            f"Error while putting object into bucket {bucket_name} with key {object_name} : {e}")
        raise e


def delete_object_from_bucket(bucket_name, object_name):
    try:
        return s3.delete_object(Bucket=bucket_name, Key=object_name)
    except Exception as e:
        logger.error(
            f"Error while deleting object from bucket {bucket_name} with key {object_name} : {e}")
        raise e
