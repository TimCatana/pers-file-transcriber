def saveTranscript(text, filename):
    textFileName = "files/outputs/" + filename + ".txt"

    with open(textFileName, "w") as f:
        f.write(text)

    print("transcription saved to: " + textFileName)
