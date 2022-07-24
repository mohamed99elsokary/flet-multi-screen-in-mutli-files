from flet import AppBar, ElevatedButton, Text, View, colors


def home(page):
    page.views.append(
        View(
            "/",
            [
                AppBar(title=Text("Flet app"), bgcolor=colors.SURFACE_VARIANT),
                ElevatedButton("Visit Store", on_click=lambda _: page.go("/store")),
            ],
        )
    )
