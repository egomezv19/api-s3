import boto3

def lambda_handler(event, context):
    # Suponemos que el bucket_name está en event['body']['bucket_name']
    bucket_name = event['body']['bucket_name']
    
    # Crear cliente de S3
    s3 = boto3.client('s3')
    
    # Crear el bucket
    response = s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'us-east-1'  # Cambia la región si es necesario
        }
    )
    
    # Retornar la respuesta
    return {
        'statusCode': 200,
        'body': f'Bucket {bucket_name} creado exitosamente'
    }
