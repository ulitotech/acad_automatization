import importlib.util
from flet import Page, app

from assets.settings import *

settings: Settings = load_settings()
_moduleList = {}


for root, dirs, _ in os.walk(r'./'):
    for dir in dirs:
        if dir == 'pages':
            for filename in os.listdir(dir):
                _file = os.path.join(dir, filename)
                if os.path.isfile(_file):
                    filename = filename.strip('.py')
                    _moduleList['/' + filename] = importlib.util.spec_from_file_location(filename, _file)


def main(page: Page):
    page.title = 'Project killer'
    page.window_width = page.window_min_width = \
        page.window_max_width = settings.window_size['w']
    page.window_height = page.window_min_height = \
        page.window_max_height = settings.window_size['h']
    page.fonts = settings.fonts[0]

    def route_change(route):
        page.views.clear()
        for key in _moduleList:
            if page.route == key:
                page.views.append(_moduleList[key].loader.load_module()._view_())

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    page.views.append(_moduleList['/first_page'].loader.load_module()._view_())
    page.update()


if __name__ == '__main__':
    app(target=main)
