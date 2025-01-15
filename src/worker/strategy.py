from worker.youtube import Youtube

class MessageStrategy:
    @staticmethod
    def get_strategy(message):
        if message.audio:
            return AudioMessageStrategy()
        elif message.video:
            return VideoMessageStrategy()
        elif message.text:
            return TextMessageStrategy()
        elif message.youtube_url:
            return YoutubeURLStrategy()
        else:
            return DefaultMessageStrategy()


class TextMessageStrategy:
    def execute(self, message):
        # Implementação de resumo de texto
        return "Texto resumido"


class VideoMessageStrategy:
    def execute(self, message):
        # Implementação de processamento de vídeo
        return "Vídeo resumido"


class AudioMessageStrategy:
    def execute(self, message):
        # Implementação de processamento de áudio
        return "Áudio resumido"


class YoutubeURLStrategy:
    def execute(self, message):
        url = message.youtube_url
        if not url:
            return "URL do YouTube não encontrada na mensagem."

        try:
            youtube = Youtube()
            video_path = youtube.download_video(url)

            return f"Vídeo baixado com sucesso em: {video_path}"
        except ValueError:
            return "A URL fornecida é inválida."
        except Exception as e:
            return f"Ocorreu um erro ao tentar baixar o vídeo: {str(e)}"


class DefaultMessageStrategy:
    def execute(self, message):
        return "Mensagem não processada"
