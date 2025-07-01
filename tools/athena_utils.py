import boto3
import time
import pandas as pd


def create_athena_client(aws_access_key, aws_secret_key, region='us-east-1'):
    return boto3.client(
        'athena',
        region_name=region,
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key
    )

def start_query(athena_client, query, database, output_location):
    response = athena_client.start_query_execution(
        QueryString=query,
        QueryExecutionContext={'Database': database},
        ResultConfiguration={'OutputLocation': output_location}
    )
    return response['QueryExecutionId']

def wait_for_query(athena_client, query_execution_id, poll_interval=2):
    while True:
        result = athena_client.get_query_execution(QueryExecutionId=query_execution_id)
        status = result['QueryExecution']['Status']['State']

        if status in ['SUCCEEDED', 'FAILED', 'CANCELLED']:
            return status
        time.sleep(poll_interval)

def get_query_results(athena_client, query_execution_id, max_results=1000):
    return athena_client.get_query_results(
        QueryExecutionId=query_execution_id,
        MaxResults=max_results
    )

def save_results_to_file(results, output_path):
    with open(output_path, 'w') as f:
        for row in results['ResultSet']['Rows']:
            f.write(','.join([col.get('VarCharValue', '') for col in row['Data']]) + '\n')
    return output_path

def athena_results_to_dataframe(results):
    rows = results['ResultSet']['Rows']
    headers = [col['VarCharValue'] for col in rows[0]['Data']]
    data = []

    for row in rows[1:]:  # Skip header row
        data.append([col.get('VarCharValue', '') for col in row['Data']])

    df = pd.DataFrame(data, columns=headers)
    return df

