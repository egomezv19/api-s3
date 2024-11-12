import boto3
import json

def lambda_handler(event, context):
    # Decodificar el cuerpo JSON
    body = json.loads(event['body'])
    bucket_name = body['bucket_name']
    
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
        'body': json.dumps({
            'message': f'Bucket {bucket_name} creado exitosamente',
            'Location': response.get('Location')
        })
    }
