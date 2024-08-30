import os
from conversaoTexto_Audio import escolher_arquivo_json

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = escolher_arquivo_json()

from google.cloud import texttospeech

# Inicializa o cliente da API
client = texttospeech.TextToSpeechClient()

# Configura o texto a ser sintetizado
synthesis_input = texttospeech.SynthesisInput(text="Olá, como posso ajudar você hoje?")

# Configura a voz (língua, gênero, etc.)
voice = texttospeech.VoiceSelectionParams(
    language_code="pt-BR",
    ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

# Configura o tipo de áudio de saída
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Executa a síntese
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# Salva o áudio em um arquivo
with open("output.mp3", "wb") as out:
    out.write(response.audio_content)
    print("Áudio salvo em 'output.mp3'")