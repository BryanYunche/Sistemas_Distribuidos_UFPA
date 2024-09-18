from conversaoTexto import ClienteTextoAudio

# Exemplo de uso da classe ClienteTextoAudio

# Caminho para o arquivo JSON com a chave da API do Google Cloud
chave_google = r"C:\\Users\\Bryan\\Documents\\Primeiro_Semestre_2024\\Sistemas_Distribuidos_UFPA\\Trabalhos_Praticos\\Trabalho_03\\chavesAPI\\apiKey.json"

# Texto que será convertido em áudio
texto_usuario = '''Esta aplicação visa resolver o desafio de transformar textos em áudio de forma natural e eficiente, uma demanda crescente em contextos educacionais e profissionais. Para isso, utiliza-se a avançada tecnologia de processamento de linguagem natural, oferecida pela API "Natural Language" do Google Cloud. A conversão de texto em áudio será realizada através da API "Text-to-Speech", também do Google Cloud. Ambas as APIs irão se integrar para processar o texto inserido pelo usuário, ajustando dinamicamente os parâmetros de síntese de voz da segunda API, de modo a garantir uma conversão natural e personalizada.

O serviço será disponibilizado por meio de um bot no Telegram, proporcionando uma forma acessível e eficaz de converter textos em áudio. A principal motivação do projeto está na ampla gama de aplicações para os áudios gerados, com destaque para a prática de estudos. Resumos acadêmicos convertidos em áudio, por exemplo, facilitam a assimilação de conteúdo e promovem novas formas de aprendizado, tornando o processo mais dinâmico e flexível. A proposta atende às necessidades de estudantes e profissionais que buscam otimizar o tempo e métodos de estudo, oferecendo uma ferramenta que alia tecnologia avançada à acessibilidade e praticidade.

'''

# ID do usuário para nomear o arquivo de áudio gerado
iDUserTelegram = "Bryan"

# Cria uma instância da classe ClienteTextoAudio com as credenciais e texto fornecidos
cliente = ClienteTextoAudio(chave_google, texto_usuario, iDUserTelegram)

# Converte o texto em áudio e salva o arquivo
cliente.salvaAudio()




