import json
import boto3
import urllib.request
from datetime import datetime

def lambda_handler(event, context):
    # Download insurance data from HTTP
    with urllib.request.urlopen("https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv") as response:
        csv_data = response.read().decode('utf-8')
    
    # Convert CSV to JSON
    lines = csv_data.strip().split('\n')
    headers = lines[0].split(',')
    
    insurance_data = []
    for line in lines[1:]:
        values = line.split(',')
        record = {}
        for i, header in enumerate(headers):
            record[header] = values[i]
        insurance_data.append(record)
    
    # Upload to S3
    client = boto3.client('s3')
    filename = "insurance_raw_" + str(datetime.now()) + ".json"
    
    client.put_object(
        Bucket="insurance-etl-datalake-antariksh",  # UPDATE THIS
        Key="raw_data/to_processed/" + filename,
        Body=json.dumps(insurance_data)
    )
