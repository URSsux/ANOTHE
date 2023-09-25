from google.oauth2 import service_account
from googleapiclient.discovery import build
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import base64

# Charger les informations d'authentification depuis le fichier JSON
client_json_file = 'client-secret.json'
credentials = service_account.Credentials.from_service_account_file(
    filename=client_json_file,
    scopes=['https://www.googleapis.com/auth/gmail.send']
)

# Créer le service Gmail en utilisant build
service_gmail = build('gmail', 'v1', credentials=credentials)

# Créer le message
message = MIMEMultipart()
message['to'] = 'sarandriarivelo@gmail.com'
message['subject'] = 'coucou'
message.attach(MIMEText('COUCOU', 'plain'))

# Convertir le message en chaîne RAW
raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')

# Envoyer le message
try:
    message = service_gmail.users().messages().send(userId='ursularandriarivelo@gmail.com', body={'raw': raw_message}).execute()
    print("E-mail envoyé avec succès!")
except Exception as e:
    print("Erreur lors de l'envoi de l'e-mail:", str(e))
