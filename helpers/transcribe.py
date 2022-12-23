import requests
from constants.constants import TRANSCRIBE_ENDPOINT, HEADERS

# transcribes the audio file uploaded
def transcribe(audioURL):
    json = {"audio_url": audioURL}
    response = requests.post(TRANSCRIBE_ENDPOINT, json=json, headers=HEADERS)
    # print(response.json())
    return response.json()['id']
