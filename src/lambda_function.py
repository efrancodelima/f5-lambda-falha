import urllib.request
import json
import boto3
import os
import zipfile
from io import BytesIO

def lambda_handler(event, context):
    # Pega o id do job
    job_id = event.get("detail", {}).get("jobId")
    print(f"job_id: {job_id}")

    # Pega o código do erro
    error_code = event.get("detail", {}).get("errorCode")
    print(f"error_code: {errorCode}")

    # Pega a mensagem de erro
    error_message = event.get("detail", {}).get("errorMessage")
    print(f"error_message: {errorMessage}")

    # Informa o microsserviço que o job falhou
    print("Enviando notificação ao servidor sobre a falha do job...")
    service_url = "http://44.204.140.237:8080/video/falha"
    data = {
        "jobId": job_id,
        "error_code": error_code,
        "error_message": error_message
    }
    json_data = json.dumps(data).encode('utf-8')
    request = urllib.request.Request(service_url, data=json_data, method="PATCH")
    request.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(request) as response:
            response_body = response.read().decode('utf-8')
            print("Servidor notificado com sucesso!")
    except urllib.error.HTTPError as e:
        print(f"Erro HTTP: {e.code}")
        print("Detalhes:", e.read().decode('utf-8'))
    except urllib.error.URLError as e:
        print(f"Erro de conexão: {e.reason}")

    # Finaliza/retorna
    return {
        'statusCode': 200,
        'body': json.dumps(f"Processo finalizado.")
    }