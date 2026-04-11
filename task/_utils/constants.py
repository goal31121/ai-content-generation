import os

DIAL_URL = 'https://ai-proxy.lab.epam.com'
DIAL_CHAT_COMPLETIONS_ENDPOINT = DIAL_URL + '/openai/deployments/{model}/chat/completions'
apikey = os.getenv('DIAL_apikey', '')