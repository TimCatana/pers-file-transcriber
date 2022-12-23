import requests
from constants.constants import TRANSCRIBE_ENDPOINT, HEADERS

def deleteUploadedFile(transcriptId):
    deleteEndpoint = TRANSCRIBE_ENDPOINT + '/' + transcriptId
    response = requests.delete(deleteEndpoint, headers=HEADERS)
    return response.json()
