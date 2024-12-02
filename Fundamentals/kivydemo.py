from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.video import Video
from kivy.graphics import Rectangle, Color
from kivy.uix.widget import Widget

class CanvasDrawing(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(1, 0, 0, 1)  # Red color
            Rectangle(pos=(50, 50), size=(100, 100))  # Draw a red rectangle

class MyApp(App):
    def build(self):
        layout = GridLayout(cols=2)  # Create a grid layout with 2 columns

        # Video player widget
        video = Video(source='video.mp4', state='play', options={'eos': 'stop'})
        layout.add_widget(video)

        # Image widget
        image = Image(source='background.png')
        layout.add_widget(image)

        # Drawing on canvas
        drawing_widget = CanvasDrawing(size=(200, 200), pos=(0, 0))
        layout.add_widget(drawing_widget)

        # Label widget
        label = Label(text='Kivy Example', size_hint=(None, None), size=(200, 50))
        layout.add_widget(label)

        return layout

if __name__ == '__main__':
    MyApp().run()
