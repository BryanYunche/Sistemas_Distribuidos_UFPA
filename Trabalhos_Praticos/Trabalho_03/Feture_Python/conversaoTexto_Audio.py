import openai
from playsound import playsound


def conversaoAudio_Texto(chaveAPI, texto):
    openai.api_key = chaveAPI
    pass

def reproduzArquivoDeAudio(audioMP3):
    playsound(audioMP3)
    pass

