# import libraries
# Directories manipulation
import os
import shutil

# Speech recognition
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence

file_path = './'
file_name = 'audio_only.wav'  # put here file in .wav format


def get_large_audio_transcription(path):
    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """
    r = sr.Recognizer()
    # open the audio file using pydub
    sound = AudioSegment.from_wav(path)
    # split audio sound where silence is 700 milliseconds or more and get chunks
    chunks = split_on_silence(sound,
                              # experiment with this value for your target audio file
                              min_silence_len=1000,
                              # adjust this per requirement
                              silence_thresh=sound.dBFS - 50,
                              # keep the silence for 1 second, adjustable as well
                              keep_silence=100
                              )

    folder_name = "audio-chunks"
    # create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    else:
        shutil.rmtree(folder_name)
        os.mkdir(folder_name)

    whole_text = ""
    # process each chunk
    progress = len(chunks)
    print("Progress: " + " " * progress + " 0%")
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the folder_name directory.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # recognize the chunk
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # try converting it to text
            try:
                text = r.recognize_google(audio_listened, language="ru-RU")
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                whole_text += text
        print("Progress: " + "#" * i + " " * (progress - i) + f" {int(i / progress * 100)}%")
    # return the text for all chunks detected
    return whole_text


result_text = get_large_audio_transcription(file_path + file_name)
with open(file_path + 'result.txt', 'w') as f:
    f.write(result_text)
