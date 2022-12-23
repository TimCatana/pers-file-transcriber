from constants.api_secrets import API_KEY_ASSEMBLYAI

UPLOAD_ENDPOINT = 'https://api.assemblyai.com/v2/upload'
TRANSCRIBE_ENDPOINT = "https://api.assemblyai.com/v2/transcript"
HEADERS = {'authorization': API_KEY_ASSEMBLYAI}
VALID_EXTENSIONS = [".mp4", ".wav"]
