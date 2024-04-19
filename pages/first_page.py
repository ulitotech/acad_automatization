from flet import Row, Column, View, Text, \
    MainAxisAlignment, FilePicker, FilePickerResultEvent
from pages.addons import settings, Book, Status, NextButton, set_page_settings

status = Status()
next_button = NextButton()


@set_page_settings(status, next_button, '/second_page')
def get_path(e: FilePickerResultEvent):
    pass


my_dialog = FilePicker(on_result=get_path)
book_button = Book(my_dialog)


def _view_():
    return View(
        '/first_page',
        controls=[
            Column([
                    Row([my_dialog,
                         Text(settings.step_description['1step'], font_family='8bit',
                              size=20, color=settings.colors[2]),
                         status,
                         ],
                        alignment=MainAxisAlignment.CENTER),
                    Row([book_button,
                         ],
                        alignment=MainAxisAlignment.CENTER,
                        ),
                    Row([next_button,
                         ],
                        alignment=MainAxisAlignment.CENTER,
                        )
                    ], spacing=2)
        ],
        bgcolor=settings.colors[1])


if __name__ == '__main__':
    pass
