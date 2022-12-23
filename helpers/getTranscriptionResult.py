import requests
import time
from constants.constants import TRANSCRIBE_ENDPOINT, HEADERS


# polls the transcription endpoint to get the result
def poll(transcriptId):
    pollingEndpoint = TRANSCRIBE_ENDPOINT + '/' + transcriptId
    response = requests.get(pollingEndpoint, headers=HEADERS)
    return response.json()


# does the poll every few seconds
def getTranscriptionResult(transcriptId):
    while True:
        response = poll(transcriptId)

        if response['status'] == 'completed':
            return response, None
        elif response['status'] == 'error':
            return response, response['error']

        print("still working... 5 seconds until next poll")
        time.sleep(5)
