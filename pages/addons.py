from flet import Image, Container, ImageFit, alignment, Audio, audio
from assets.settings import load_settings
from gui_logic import states

settings = load_settings()


def set_page_settings(status, next_button, next_page=None):
    def decorator(func):
        def wrapper(*args):
            response = args[0]
            elem = None
            if next_page == '/second_page':
                elem = 0
            elif next_page == '/third_page':
                elem = 1
            elif next_page is None:
                elem = 2
            if response.path is not None:
                status.src = settings.images['icons']['ok']
                states['statuses'][elem] = 1
                states['paths'][elem] = response.path
                if next_page is not None:
                    next_button.image_src = settings.images['icons']['next']
                    next_button.on_hover = next_button.hover_next
                    next_button.on_click = lambda _: response.page.go(next_page)
                    next_button.update()
                else:
                    next_button.image_src = settings.images['icons']['press_start_color']
                    next_button.on_hover = next_button.hover_start
                    next_button.on_click = lambda e: StartButton.start_work(e)
                    next_button.update()
            elif response.path is None and states['statuses'][elem] == 1:
                pass
            status.update()
            func(*args)

        return wrapper

    return decorator


class Status(Image):
    def __init__(self):
        super().__init__()
        self.src = settings.images['icons']['not_ok']
        self.width = 20


class StartButton(Container):
    def __init__(self):
        super().__init__()
        self.width = 100
        self.height = 50
        self.image_src = settings.images['icons']['press_start_bw']
        self.image_fit = ImageFit.CONTAIN

    def hover_start(self, e):
        if e.data == 'true':
            self.image_src = settings.images['icons']['press_start_color_light']
        else:
            self.image_src = settings.images['icons']['press_start_color']
        self.update()

    @staticmethod
    def start_work(e):
        print(f"START!!!\n{states['paths']}")


class Book(Container):
    def __init__(self, my_dialog):
        super().__init__()
        self.my_dialog = my_dialog
        self.width = 80
        self.height = 70
        self.image_src = settings.images['icons']['closed_book']
        self.on_click = lambda _: self.my_dialog.get_directory_path()
        self.image_fit = ImageFit.CONTAIN
        self.on_hover = self.hover_book

    def hover_book(self, e):
        if e.data == 'true':
            self.image_src = settings.images['icons']['book']
        else:
            self.image_src = settings.images['icons']['closed_book']
        self.update()


class NextButton(Container):
    def __init__(self):
        super().__init__()
        self.width = 110
        self.height = 40
        self.image_src = settings.images['icons']['next_bw']
        self.image_fit = ImageFit.CONTAIN
        self.alignment = alignment.center

    def hover_next(self, e):
        if e.data == 'true':
            self.image_src = settings.images['icons']['next_light']
        else:
            self.image_src = settings.images['icons']['next']
        self.update()

audio1 = Audio(src='../assets/images/audio.mp3',
                            autoplay=True, release_mode=audio.ReleaseMode.LOOP)
class AudioIcon(Container):
    def __init__(self, player):
        super().__init__()
        self.image_src = settings.images['icons']['music_on']
        self.width = 40
        self.height = 40
        self.player = player
        self.on_click = self.turn_audio

    def turn_audio(self, e):
        if states['volume'] == True:
            self.player.pause()
            self.image_src = settings.images['icons']['music_off']
            states['volume'] = False
            self.update()
        else:
            states['volume'] = True
            self.player.resume()
            self.image_src = settings.images['icons']['music_on']
            self.update()


audio_icon = AudioIcon(audio1)
