from botocore.exceptions import ClientError, ParamValidationError
from moto import mock_redshiftdata
import pytest

import boto3
from app import redshift_operations


@pytest.fixture
def redshift_data_client():
    yield boto3.client('redshift-data', region_name='us-east-1')


@mock_redshiftdata
def test_execute_statement_with_parameters(redshift_data_client):
    cluster_id = 'test-cluster'
    database = 'test-db'
    sql = 'select * from test_table where id = :id'
    parameters = [{'name': 'id', 'value': {'stringValue': '1'}}]
    with pytest.raises(ParamValidationError) as raised_exception:
        redshift_operations.execcute_statement(sql=sql,cluster_id=cluster_id,database=database,database_user="user",parameters=parameters)
    assert_exception_message(raised_exception, "Parameter validation failed")


def assert_exception_message(raised_exception, message):
    assert message in str(raised_exception.value)
