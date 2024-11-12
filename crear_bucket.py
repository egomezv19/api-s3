import boto3

def lambda_handler(event, context):
    # Obtener el nombre del bucket directamente desde event['body'] sin usar json
    body = event['body']
    bucket_name = eval(body)['bucket_name']  # Utiliza eval() para extraer el campo bucket_name del string JSON

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
