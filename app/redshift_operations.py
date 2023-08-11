import boto3
from logging import getLogger, INFO

logger = getLogger(__name__)
logger.setLevel(INFO)

redshift_data = boto3.client('redshift-data', region_name='us-east-1')


def execute_statement(sql, cluster_id, database, database_user,stmt_name):
    try:
        response = redshift_data.execute_statement(
            ClusterIdentifier=cluster_id,
            Database=database,
            DbUser=database_user,
            Sql=sql,
            StatementName=stmt_name,
            WithEvent=True,
            )
        return response
    except Exception as e:
        logger.error(e)
        raise e

