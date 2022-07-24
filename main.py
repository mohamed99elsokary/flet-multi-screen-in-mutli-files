import flet
from flet import Page

from page_handler import page_handler


def main(page: Page):
    page.title = "multi screen files example"

    def route_change(route):
        page.views.clear()
        page_handler(page)

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go(page.route)


flet.app(target=main)
