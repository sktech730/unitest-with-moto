from botocore.exceptions import ClientError, ParamValidationError
from moto import mock_redshiftdata
import pytest

import boto3
from app import redshift_operations


@pytest.fixture
def redshift_data_client():
    yield boto3.client('redshift-data', region_name='us-east-1')


@mock_redshiftdata
def test_execute_statement_with_invalid_parameters(redshift_data_client):
    cluster_id = 'test-cluster'
    database = 'test-db'
    sql = 'select * from test_table where id = 100'
    stmt_name = "sample_stmt_name"
    with pytest.raises(ParamValidationError) as raised_exception:
        redshift_operations.execute_statement(sql=None, cluster_id=cluster_id,
                                              database=database, database_user="user",
                                              stmt_name=stmt_name)
    assert_exception_message(raised_exception, "Parameter validation failed")


@mock_redshiftdata
def test_execute_statement(redshift_data_client):
    cluster_id = 'test-cluster'
    database = 'test-db'
    sql = 'select * from test_table where id = 100'
    stmt_name = "sample_stmt_name"
    response = redshift_operations.execute_statement(sql=sql, cluster_id=cluster_id,
                                                     database=database,
                                                     database_user="user",
                                                     stmt_name=stmt_name)
    describe_response = redshift_data_client.describe_statement(Id=response["Id"])
    assert describe_response["ClusterIdentifier"] == cluster_id
    assert describe_response["Database"] == database
    assert describe_response["DbUser"] == "user"
    assert describe_response["QueryString"] == sql
    assert describe_response["Status"] == "STARTED"


def assert_exception_message(raised_exception, message):
    assert message in str(raised_exception.value)
