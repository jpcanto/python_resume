import os
import re

from pytubefix import YouTube as YT


class Youtube:
    def download_video(self, url):
        is_url_valid = self.validate_url(url)

        if not is_url_valid:
            raise ValueError("URL inválida")

        _output_path = rf"{os.path.expanduser('~')}\Videos\pr_audios"

        if not os.path.exists(_output_path):
            os.makedirs(_output_path)
            print(f"Pasta {_output_path} criada")

        try:
            yt = YT(url)
            stream = yt.streams.get_audio_only()
            print(f"Vídeo encontrado: {yt.title}")
        except Exception as e:
            print(f"Erro ao obter vídeo: {str(e)}")
            raise e

        _title = yt.title
        title = re.sub(r'[<>:"/\\|?*]', "", _title)
        title = title.replace("'", "")
        title = title.strip().replace(" ", "_")
        title = f"_{title}.mp3"

        output_path = stream.download(_output_path, title)
        print(f"baixando {output_path} em '{output_path}'")
        output_path = f"{output_path}/{title}"
        print(f"Áudio baixado em {output_path}")

        return output_path

    def validate_url(self, url):
        # Regex para validar URLs do YouTube (normais e de shorts)
        youtube_regex = r"^(https://(?:www\.)?youtube\.com/(?:watch\?v=[a-zA-Z0-9_-]{11}|shorts/[a-zA-Z0-9_-]+))$"
        return re.match(youtube_regex, url) is not None
