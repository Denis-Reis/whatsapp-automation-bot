from flask import Flask, request
import requests

app = Flask(__name__)

ACCESS_TOKEN = "EAASBMDfVVRYBRPqPo4ZCh5zBMjmParusBdLRBccBPdken7qOv60lRDUH7wjkS9teBPqrBWiOOHAwSZCO0DDb2TB35ZB3klr1bakjcwiYjMUtZAKXGtc2eZCkrXLZABN6sdqNf8k2RpCtznUB6Lbfi5KkAbRxTqfXOuYmGkDqKS3IIFs0NQ4xaxwQd2nGiQspJu8kQaXUOomiZBPASn7VJf1daj1AZCdr71ZBqhwy9u47HRlu99N6U4aPTpZCyR8lZB04Tg7JYJnVWbnZAOTLtKJrv4SLCyfzLQZDZD"
PHONE_NUMBER_ID = "1012538745285014"

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        verify_token = "denilson123"
        if request.args.get("hub.verify_token") == verify_token:
            return request.args.get("hub.challenge")
        return "Token inválido", 403
    
    if request.method == "POST":
        data = request.json
        print("Mensagem recebida:", data)

        if "messages" in data["entry"][0]["changes"][0]["value"]:
            msg = data["entry"][0]["changes"][0]["value"]["messages"][0]
            from_number = msg["from"]

            enviar_resposta(from_number, "Olá, recebi sua mensagem! 🚀")

        return "EVENT_RECEIVED", 200

def enviar_resposta(to, mensagem):
    url = f"https://graph.facebook.com/v17.0/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": mensagem}
    }
    response = requests.post(url, headers=headers, json=payload)
    print("Resposta enviada:", response.json())

if __name__ == "__main__":
    app.run(port=5000)


    