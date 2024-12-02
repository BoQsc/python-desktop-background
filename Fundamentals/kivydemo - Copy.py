from kivy.app import App
from kivy.uix.videoplayer import VideoPlayer

class VideoApp(App):
    def build(self):
        # Directly return the VideoPlayer widget to play 'video.mp4'
        return VideoPlayer(source='video.mp4', state='play')

if __name__ == '__main__':
    VideoApp().run()
