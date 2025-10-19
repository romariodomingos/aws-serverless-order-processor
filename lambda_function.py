import json
import boto3
from decimal import Decimal

# Inicializa os clientes AWS
dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')

# Nome da tabela DynamoDB e ARN do SNS
TABLE_NAME = 'OrdersTable'
SNS_TOPIC_ARN = 'arn:aws:sns:REGIAO:ID_DA_CONTA:OrderNotificationTopic'

table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    """
    Processa mensagens SQS, grava no DynamoDB e envia alerta SNS.
    """
    for record in event['Records']:
        body = json.loads(record['body'])
        order_id = str(body.get('orderId'))
        customer = body.get('customer')
        amount = Decimal(str(body.get('amount', 0)))

        # Salva o pedido no DynamoDB
        table.put_item(Item={
            'orderId': order_id,
            'customer': customer,
            'amount': amount
        })

        # Cria e envia mensagem SNS
        message = (
            f" Novo pedido processado!\n"
            f" ID: {order_id}\n"
            f" Cliente: {customer}\n"
            f" Valor: ${amount}"
        )

        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=message,
            Subject="Novo Pedido Processado "
        )

        print(f"Pedido {order_id} salvo no DynamoDB e notificação SNS enviada!")

    return {
        "statusCode": 200,
        "body": json.dumps("Mensagens processadas e notificações enviadas com sucesso!")
    }
