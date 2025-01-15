class Message:
    def __init__(self, youtube_url=None, text=None, audio=None, video=None):
        self.youtube_url = youtube_url
        self.text = text
        self.audio = audio
        self.video = video
