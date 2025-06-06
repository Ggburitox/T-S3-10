import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    # Entrada (json)
    print(event)
    tenant_id = event['body']['tenant_id']
    alumno_id = event['body']['alumno_id']
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')
    response = table.delete_item(
        Key={
            'tenant_id': tenant_id,
            'alumno_id': alumno_id
        },
        ReturnValues='ALL_OLD'
    )
    deleted_item = response.get('Attributes')
    print('Respuesta:', deleted_item)

    # Salida
    if deleted_item:
        return {
            'statusCode': 200,
            'tenant_id': tenant_id,
            'alumnos': [alumno_id]
        }
    else:
        return {
            'statusCode': 404,
            'mensaje': 'Registro no encontrado',
            'tenant_id': tenant_id
        }