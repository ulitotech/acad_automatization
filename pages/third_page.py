from flet import FilePickerResultEvent, FilePicker, Column, Row, Text, \
    MainAxisAlignment, View
from pages.addons import settings, StartButton, Status, Book, set_page_settings

status = Status()
start_button = StartButton()


@set_page_settings(status, start_button)
def get_path(e: FilePickerResultEvent):
    pass


my_dialog = FilePicker(on_result=get_path)
book_button = Book(my_dialog)


def _view_():
    return View(
        '/third_page',
        controls=[my_dialog,
                  Column([
                      Row([
                          Text(settings.step_description['3step'], font_family='8bit',
                               size=20, color=settings.colors[2]),
                          status,
                      ],
                          alignment=MainAxisAlignment.CENTER, ),
                      Row([
                          book_button
                      ],
                          alignment=MainAxisAlignment.CENTER,
                      ),
                      Row([
                          start_button,
                      ],
                          alignment=MainAxisAlignment.CENTER,
                      )
                  ], spacing=5)
                  ],
        bgcolor=settings.colors[1])
