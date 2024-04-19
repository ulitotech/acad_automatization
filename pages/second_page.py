from flet import FilePickerResultEvent, FilePicker, Row, Column, View, Text, MainAxisAlignment
from pages.addons import settings, Status, NextButton, Book, set_page_settings

status = Status()
next_button = NextButton()


@set_page_settings(status, next_button, '/third_page')
def get_path(e: FilePickerResultEvent):
    pass


my_dialog = FilePicker(on_result=get_path)
book_button = Book(my_dialog)


def _view_():
    return View(
        '/second_page',
        controls=[
                  Column([
                      Row([my_dialog,
                           Text(settings.step_description['2step'], font_family='8bit',
                                size=20, color=settings.colors[2]),
                           status,
                           ],
                          alignment=MainAxisAlignment.SPACE_AROUND, ),
                      Row([book_button],
                          alignment=MainAxisAlignment.CENTER,
                          ),
                      Row([
                          next_button
                      ],
                          alignment=MainAxisAlignment.CENTER,
                      )
                  ], spacing=5)
                  ],
        bgcolor=settings.colors[1])
