from flet import AppBar, ElevatedButton, Text, View, colors


def store(page):
    page.views.append(
        View(
            "/store",
            [
                AppBar(title=Text("Store"), bgcolor=colors.SURFACE_VARIANT),
                ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
            ],
        )
    )
