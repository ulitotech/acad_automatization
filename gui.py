from flet import app, Page, Text, Container, ImageFit, alignment, Row, Column, Image, FilePicker, \
    FilePickerResultEvent, border, MainAxisAlignment, ControlEvent, Audio, audio
from assets.settings import *

settings = load_settings()


class StartButton(Row):
    """Class for describing button for starting app"""

    def __init__(self):
        super().__init__()
        self.controls = [Container(width=100, height=50, image_src=settings.images['icons']['press_start_color'],
                                   image_fit=ImageFit.CONTAIN,
                                   on_click=self.start_process, visible=False,
                                   on_hover=lambda e: self.hover_start(e)), ]
        self.alignment = MainAxisAlignment.END
        self.expand = 9


    @staticmethod
    def start_process(e: ControlEvent) -> dict:
        """Getting dict with paths for working app"""
        print(App().PATHS)

    def hover_start(self, e: ControlEvent) -> None:
        """Reaction on hovering"""
        if e.data == 'true':
            self.controls[0].image_src = settings.images['icons']['press_start_color_light']
        else:
            self.controls[0].image_src = settings.images['icons']['press_start_color']
        self.update()


start_button = StartButton()


class Item(Column):
    def __init__(self, text: str):
        super().__init__()
        self.path: Container = None
        self.book: Container = None
        self.cross: Image = None
        self.my_dialog: FilePicker = FilePicker(on_result=self.get_path)
        self.text: str = text
        self.cross: Image = Image(src=settings.images['icons']['not_ok'],
                                  width=25, data=False)
        self.text: Text = Text(self.text, font_family='8bit',
                               size=20, color=settings.colors[2])
        self.book: Container = Container(width=50, height=40,
                                         image_src=settings.images['icons']['closed_book'],
                                         image_fit=ImageFit.CONTAIN,
                                         on_hover=self.hover_book,
                                         on_click=lambda _: self.my_dialog.get_directory_path())
        self.path: Container = Container(height=40, expand=True, content=Text(value='Тут пока что ничего нет...',
                                                                              color=settings.colors[3],
                                                                              font_family='8bit', size=18, max_lines=1),
                                         border=border.all(width=2, color=settings.colors[3]),
                                         alignment=alignment.center_left)
        self.spacing: int = 1
        self.controls: list[Row] = [Row([self.text, self.my_dialog]), Row([self.cross, self.path, self.book])]

    def get_path(self, e: FilePickerResultEvent):
        """Function for changing parameters in objects after getting paths"""
        if e.path is not None:
            self.path.content.value = e.path
            self.cross.src = settings.images['icons']['ok']
            self.cross.data = True
            App().add_path(self, e.path)
            self.path.update()
            self.cross.update()
        if len(App.PATHS.keys()) == 3:
            start_button.controls[0].image_src = settings.images['icons']['press_start_color']
            start_button.controls[0].visible = True
            start_button.update()

    def hover_book(self, e: ControlEvent):
        """Reaction on hovering"""
        if e.data == 'true':
            self.book.image_src = settings.images['icons']['book']
        else:
            self.book.image_src = settings.images['icons']['closed_book']
        self.update()


class App(Column):
    PATHS = {}

    def __init__(self):
        super().__init__()
        self.start_button = start_button
        self.controls = [Item(step_description[f'{i + 1}step']) for i in range(3)]
        self.controls.append(Row([self.start_button,AudioPlayer(settings.sounds[0])]))
        self.spacing = 1

    @classmethod
    def add_path(cls, item: Item, path: str):
        cls.PATHS[id(item)] = path


class AudioPlayer(Container):
    def __init__(self, path: str):
        super().__init__()
        self.path = path
        self.width = self.height = 50
        self.status = True
        self.content = Audio(src=self.path, volume=0.7, release_mode=audio.ReleaseMode.LOOP, autoplay=True)
        self.image_src = settings.images['icons']['music_on']
        self.on_click = self.on_off
        self.expand = 1


    def on_off(self, e:ControlEvent):
        if self.status:
            self.status = False
            self.image_src = settings.images['icons']['music_off']
            self.content.pause()
            self.update()
        else:
            self.status = True
            self.content.resume()
            self.image_src = settings.images['icons']['music_on']
            self.update()




def main(page: Page):
    page.title = 'Project killer'
    page.window_width = page.window_min_width = \
        page.window_max_width = settings.window_size['w']
    page.window_height = page.window_min_height = \
        page.window_max_height = settings.window_size['h']
    page.fonts = settings.fonts[0]
    page.bgcolor = settings.colors[1]
    page.add(App())
    page.update()


if __name__ == '__main__':
    app(target=main)
