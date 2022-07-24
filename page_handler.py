from screens.home import home
from screens.store import store


def page_handler(page):
    if page.route == "/":
        home(page)
    elif page.route == "/store":
        store(page)
