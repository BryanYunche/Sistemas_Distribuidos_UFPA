import os
from google.cloud import texttospeech, language_v1

# Define a classe ClienteTextoAudio
class ClienteTextoAudio:
    # Construtor da classe
    def __init__(self, chaveGoogle, textoUsuario, IdUsuario):
        """
        Inicializa a classe com as credenciais do Google Cloud, o texto a ser convertido e o ID do usuário.
        
        :param chaveGoogle: Caminho para o arquivo JSON com a chave de autenticação do Google Cloud.
        :param textoUsuario: O texto que será convertido em áudio.
        :param IdUsuario: Identificador do usuário para nomear o arquivo de áudio.
        """
        self.chaveGoogle = chaveGoogle
        self.textoUsuario = textoUsuario
        self.IdUsuario = IdUsuario

        # Define a variável de ambiente para autenticação com a chave do Google Cloud
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = self.chaveGoogle

    # Método para analisar o sentimento do texto
    def analisar_texto(self):
        """
        Analisa o sentimento do texto usando a API de Natural Language do Google Cloud.
        
        :return: Objeto que contém a análise de sentimento do texto.
        """
        # Cria um cliente para a API de Natural Language
        client = language_v1.LanguageServiceClient()
        
        # Cria um documento com o texto para análise
        document = language_v1.Document(content=self.textoUsuario, type_=language_v1.Document.Type.PLAIN_TEXT)
        
        # Analisa o sentimento do documento
        sentiment = client.analyze_sentiment(request={"document": document}).document_sentiment
        
        return sentiment

    # Método para converter texto em áudio
    def converte_Texto_Audio(self):
        """
        Converte o texto em áudio usando a API Text-to-Speech do Google Cloud, ajustando os parâmetros com base no sentimento.
        
        :return: Conteúdo do áudio gerado.
        """
        # Analisa o sentimento do texto para ajustar os parâmetros de áudio
        sentiment = self.analisar_texto()

        # Ajusta os parâmetros de fala com base no sentimento
        speaking_rate = 1.0 + (sentiment.score * 0.5)  # A taxa de fala aumenta com a pontuação do sentimento
        pitch = sentiment.score * 2.0  # O tom da voz é ajustado com base na pontuação do sentimento

        # Cria um cliente para a API Text-to-Speech
        client = texttospeech.TextToSpeechClient()

        # Define o texto a ser convertido em áudio
        synthesis_input = texttospeech.SynthesisInput(text=self.textoUsuario)

        # Define os parâmetros da voz
        voice = texttospeech.VoiceSelectionParams(
            language_code="pt-BR",  # Define o idioma como português do Brasil
            ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL  # Define o gênero da voz como neutro
        )

        # Define os parâmetros de configuração do áudio
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3,  # Define o formato do áudio como MP3
            speaking_rate=speaking_rate,  # Define a taxa de fala ajustada
            pitch=pitch,  # Define o tom ajustado
            volume_gain_db=0.0  # Define o ganho de volume
        )

        # Converte o texto em áudio
        response = client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )

        # Retorna o conteúdo do áudio gerado
        return response.audio_content

    # Método para salvar o áudio gerado em um arquivo
    def salvaAudio(self):
        """
        Salva o áudio gerado em um arquivo MP3 na pasta 'audios_gerados', que está um nível acima do diretório do script.
        
        :return: Caminho do arquivo de áudio salvo.
        """
        # Converte o texto em áudio
        audioMP3 = self.converte_Texto_Audio()

        # Obtém o diretório onde o script está localizado
        dir_atual = os.path.dirname(__file__)
        # Define o caminho para a pasta 'audios_gerados', que está um nível acima do diretório atual do script
        caminho_pasta = os.path.join(dir_atual, "..", "audios_gerados")
        # Cria a pasta se não existir
        os.makedirs(caminho_pasta, exist_ok=True)

        # Define o caminho completo para o arquivo de áudio
        caminho_arquivo = os.path.join(caminho_pasta, f'{self.IdUsuario}_Audio.mp3')

        # Salva o áudio em um arquivo MP3
        with open(caminho_arquivo, "wb") as audio_file:
            audio_file.write(audioMP3)

        # Imprime o caminho do arquivo salvo e retorna o caminho
        print(f"Áudio salvo em: {caminho_arquivo}")
        return caminho_arquivo

