import boto3
import Logger
import os
import json
import time
import datetime


s3 = boto3.client('s3')
logger = Logger.get_logger()
logger.setLevel(Logger.INFO)
# s3-get-object
def get_object_from_bucket(bucket_name,object_name):
    try:
        return s3.get_object(Bucket=bucket_name, Key=object_name)
    except Exception as e:
        logger.error(f"Error while getting object from bucket {bucket_name} with key {object_name} : {e}")
        raise e



def put_object_into_bucket(bucket_name,object_name,data):
    try:
        return s3.put_object(Bucket=bucket_name, Key=object_name, Body=data)
    except Exception as e:
        logger.error(f"Error while putting object into bucket {bucket_name} with key {object_name} : {e}")
        raise e


def delete_object_from_bucket(bucket_name,object_name):
    try:
        return s3.delete_object(Bucket=bucket_name, Key=object_name)
    except Exception as e:
        logger.error(f"Error while deleting object from bucket {bucket_name} with key {object_name} : {e}")
        raise e

def list_objects_from_bucket(bucket_name):
    try:
        return s3.list_objects(Bucket=bucket_name)
    except Exception as e:
        logger.error(f"Error while listing objects from bucket {bucket_name} : {e}")
        raise e


def list_objects_from_bucket_with_prefix(bucket_name,prefix):
    try:
        return s3.list_objects(Bucket=bucket_name, Prefix=prefix)
    except Exception as e:
        logger.error(f"Error while listing objects from bucket {bucket_name} with prefix {prefix} : {e}")
        raise e


