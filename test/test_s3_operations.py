import pytest
import boto3
from moto import mock_s3
from app import s3_operations


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
