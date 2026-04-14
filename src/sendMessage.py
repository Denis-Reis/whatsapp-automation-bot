import requests

ACCESS_TOKEN = "EAASBMDfVVRYBRGvgXwEgKfkeMcOQRVywkotVCpfTmvuoneYSfzpwakROJAnMVJVCz5ZAPmVPZAxnFNglpZCYFF8q5zZBA4Ua1UwE9pxEDw1ZCCZAdZCpx09DcdxTKZAjyzANZCepwH2XoXQWZCBZB6vaOOn4c2X7s9ZCMuRaMf4pM2yVUWwxXSZAzIzJZA6p0rDZAtZAkyGNsYEqB8TzzDs4H7HOXoCPZCsKc0ZBPH62nP9Piu0VTatbZAa6yZCx8IFIbDeIJmIt43oxYmZBOWDcrqZA2X8nlzIZC3dHXCZA"
PHONE_NUMBER_ID = "1012538745285014"
RECIPIENT_NUMBER = "5511969115857"

url= f"https://graph.facebook.com/v17.0/{PHONE_NUMBER_ID}/messages"

headers = {
     "Authorization": f"Bearer {ACCESS_TOKEN}",
     "Content-Type": "application/json"
}

data = {

    "messaging_product": "whatsapp" , 
    "to": RECIPIENT_NUMBER,
    "type": "text",
    "text": {"body": "Olá Dennys! Este é meu primeiro Bot de TESTE "}

}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())