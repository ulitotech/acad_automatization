import flet as ft
# from time import monotonic
from assets.settings import *

settings: Settings = load_settings()

def main(page:ft.Page):
    page.window_width = page.window_min_width = \
        page.window_max_width = settings.window_size['w']
    page.window_height = page.window_min_height = \
        page.window_max_height = settings.window_size['h']
    page.bgcolor = settings.colors[1]
    page.fonts = settings.fonts[0]
    def get_path(e: ft.FilePickerResultEvent):
        print(e.path)

    my_dialog = ft.FilePicker(on_result=get_path)
    page.overlay.append(my_dialog)
    page.title = 'some_program'
    page.add(
        ft.Column([
            ft.Row([
                ft.Text('Выбери папку с шаблонами', font_family='8bit',
                        size=20, color=settings.colors[2]),
                ft.Image(src=settings.images['icons']['not_ok'], width=20, height=20),
            ],
                alignment=ft.MainAxisAlignment.CENTER,),
            ft.Row([
                ft.TextButton(content=ft.Image(src=settings.images['icons']['book']),
                              on_click=lambda _: my_dialog.get_directory_path(),
                              width=80)
            ],
                alignment=ft.MainAxisAlignment.CENTER, ),
            ft.Row([
                ft.Text('Выбери папку с исходными данными', font_family='8bit', size=20,
                        color=settings.colors[2]),
                ft.Image(src=settings.images['icons']['not_ok'], width=20, height=20),
            ],
                alignment=ft.MainAxisAlignment.CENTER,),
            ft.Row([
                ft.TextButton(content=ft.Image(src=settings.images['icons']['book']),
                              on_click=lambda _: my_dialog.get_directory_path(),
                              width=80)
            ],
                alignment=ft.MainAxisAlignment.CENTER, ),
            ft.Row([
                ft.Text('Выбери папку для сохранения проектов', font_family='8bit', size=20,
                        color=settings.colors[2]),
                ft.Image(src=settings.images['icons']['not_ok'], width=20, height=20),
            ],
                alignment=ft.MainAxisAlignment.CENTER,),
            ft.Row([
                ft.TextButton(content=ft.Image(src=settings.images['icons']['book']),
                              on_click=lambda _: my_dialog.get_directory_path(),
                              width=80)
            ],
                alignment=ft.MainAxisAlignment.CENTER, ),
            ft.Row([
                ft.Image(src=settings.images['icons']['press_start_bw'], width=100,),
            ],
                alignment=ft.MainAxisAlignment.CENTER,),
        ])
    )
    page.update()
    # img = ft.Image(src = imgs[0], width =500)
    # page.add(img)
    # t = monotonic()
    # i = 1
    # page.update()
    # def update_img_src():
    #     img.src = imgs[i]
    #     img.update()
    # while True:
    #     if monotonic() - t > 1:
    #         t = monotonic()
    #         update_img_src()
    #         page.update()
    #         if i == 3:
    #             break
    #         i += 1



ft.app(target=main, assets_dir='assets')


