import os
from dataclasses import dataclass

directory = r".\assets"
colors = {1: '#2c0242', 2: '#e95cc2', 3: '#fcb2e3',
          4: '#bd297d', 5: '#f500bd', 6: '#ff86c9'}
window_size = {"w": 550, 'h': 320}
step_description = {'1step': 'Выбери папку с шаблонами',
                    '2step': 'Выбери папку с исходными данными',
                    '3step': 'Выбери папку для сохранения проектов'}
images = {'icons': {}, 'progress': {}}
sounds = []
fonts = []


@dataclass
class Settings:
    colors: dict[int:str]
    window_size: dict[str:int]
    fonts: list[dict[str:str]]
    step_description: dict[str:str]
    images: dict[str:dict[str:str]]
    sounds: list


def load_settings() -> Settings:
    for dir, fold, file in os.walk(directory):
        if dir.endswith('fonts'):
            for f in os.listdir(dir):
                if f.endswith('.otf') or f.endswith('.ttf'):
                    fonts.append(dict([(f[:-4], os.path.join(os.path.abspath(dir), f))]))
        if dir.endswith('images'):
            for f in os.listdir(dir):
                if f.endswith('.png'):
                    if 'prog' in f:
                        images['progress'][f[:-4]] = os.path.join(dir, f)
                    else:
                        images['icons'][f[:-4]] = os.path.join(dir, f)
        if dir.endswith('sounds'):
            for f in os.listdir(dir):
                if f.endswith('.mp3'):
                    sounds.append(os.path.join(dir, f))

    return Settings(
        colors=colors,
        window_size=window_size,
        fonts=fonts,
        step_description=step_description,
        images=images,
        sounds=sounds
    )
