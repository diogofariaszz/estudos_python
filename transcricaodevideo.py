from youtube_transcript_api import YouTubeTranscriptApi
import speech_recognition as sr
import collections
import openai

# Configuração da API Key do OpenAI
openai.api_key = 'YOUR_API_KEY'

def transcrever_audio_youtube(url):
    try:
        # Obtém a transcrição do vídeo do YouTube em português
        video_id = url.split('=')[-1]
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['pt'])

        # Concatena as linhas de texto da transcrição
        texto_transcrito = ' '.join([line['text'] for line in transcript])
        return texto_transcrito
    except Exception as e:
        print(f"Erro ao obter a transcrição do vídeo: {e}")
        return None

def gerar_glossario(texto):
    try:
        # Divide o texto em palavras
        palavras = texto.split()

        # Conta a frequência das palavras
        contagem = collections.Counter(palavras)

        # Seleciona as 10 palavras mais frequentes
        glossario = [palavra for palavra, _ in contagem.most_common(10)]
        
        return glossario
    except Exception as e:
        print(f"Erro ao gerar glossário: {e}")
        return None

def main():
    # URL do vídeo do YouTube
    url = 'https://www.youtube.com/watch?v=V0uBbiEfw7s'

    # Transcreve o áudio do vídeo
    texto_transcrito = transcrever_audio_youtube(url)
    if texto_transcrito:
        print("Texto transcrito:")
        print(texto_transcrito)

        # Gera o glossário
        glossario = gerar_glossario(texto_transcrito)
        if glossario:
            print("\nGlossário:")
            for i, termo in enumerate(glossario, start=1):
                print(f"{i}. {termo}")
        else:
            print("Não foi possível gerar o glossário.")
    else:
        print("Não foi possível transcrever o áudio do vídeo.")

if __name__ == "__main__":
    main()
