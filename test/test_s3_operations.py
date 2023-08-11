import pytest
import boto3
from moto import mock_s3
from app import s3_operations
from botocore.exceptions import ClientError


@pytest.fixture
def s3():
    with mock_s3():
        yield boto3.resource('s3', region_name='us-east-1')


@mock_s3
def test_s3_get_object(s3):
    s3.create_bucket(Bucket='test-bucket')
    s3.Object('test-bucket', 'test-file').put(Body=b'Hello World!')
    obj = s3_operations.get_object_from_bucket("test-bucket", "test-file")
    assert obj['Body'].read().decode('utf-8') == 'Hello World!'


@mock_s3
def test_s3_put_object(s3):
    s3.create_bucket(Bucket='test-bucket')
    s3_operations.put_object_into_bucket("test-bucket", "test_file", "Hello World!")
    resp = s3.Object('test-bucket', 'test_file').get()
    assert resp["Body"].read().decode('utf-8') == "Hello World!"


@mock_s3
def test_s3_delete_object(s3):
    s3.create_bucket(Bucket='test-bucket')
    s3_operations.put_object_into_bucket("test-bucket", "test_file", "Hello World!")
    s3_operations.delete_object_from_bucket(bucket_name="test-bucket",object_name="test_file")
    with pytest.raises(ClientError) as raised_exception:
        s3_operations.get_object_from_bucket(bucket_name="test-bucket",object_name="test_file")
    assert raised_exception





