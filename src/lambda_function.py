import json

def lambda_handler(event, context):
    # Imprime o evento recebido no console
    print("Evento recebido:")
    print(json.dumps(event, indent=4))
    
    # Retorna uma resposta
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Evento processado com sucesso!'
        })
    }