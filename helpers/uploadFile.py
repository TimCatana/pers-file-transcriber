import requests
from constants.constants import UPLOAD_ENDPOINT, HEADERS


# uploads file to assemblyai for for transcription
def uploadFile(filename):
    file = "files/inputs/" + filename

    def read_file(file, chunk_size=5242880):
        with open(file, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data

    response = requests.post(UPLOAD_ENDPOINT,
                             headers=HEADERS,
                             data=read_file(file))

    # print(response.json())
    return response.json()['upload_url']
