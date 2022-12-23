import sys
from constants.constants import VALID_EXTENSIONS
from helpers.validateFile import validateFileExtension
from helpers.uploadFile import uploadFile
from helpers.transcribe import transcribe
from helpers.getTranscriptionResult import getTranscriptionResult
from helpers.saveTranscript import saveTranscript
from helpers.deleteUploadedFile import deleteUploadedFile


# main
if __name__ == "__main__":

    # GET THE FILE TO TRANSCRIBE

    try:
        filename = sys.argv[1]
    except IndexError:
        sys.exit(
            "ERROR - Please enter the audio file name to transcribe as the second argument")

    # CHECK IF THE FILE IS A VALID AUDIO FILE WITH A VALID EXTENSION
    isValid = validateFileExtension(filename)

    if (isValid == False):
        print(
            "ERROR - Please enter a file with a valid extention type: ")
        for i in range(len(VALID_EXTENSIONS)):
            print(VALID_EXTENSIONS[i])
        sys.exit()

    # UPLOAD AUDIO FILE TO ASSEMBLYAI
    audioURL = uploadFile(filename)

    # BEGIN ASSEMBLYAI TRANSCRIPTION
    transcriptId = transcribe(audioURL)
    print(transcriptId)

    # POLL THE TRANSCRIPTION PROGRESS UNTIL IT IS FINISHED
    result, error = getTranscriptionResult(transcriptId)

    # DELETE FILE FROM ASSEMBLY AI UPLOADS (TO PROTECT SENSITIVE FILES, MAY BE COMMENTED OUT IF YOU WANT)
    deleteUploadedFile(transcriptId)

    # SAVE TRANSCRIPT IF SUCCESS, PRINT ERROR IT NOT
    if (error == None):
        saveTranscript(result['text'], filename)
    else:
        print("Something went wrong with the transcription, please try again")
        sys.exit("ERROR: " + error)
