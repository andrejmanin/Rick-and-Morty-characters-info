import flet as ft

import connection
import fist_seen
import last_location_text
import top_text

def cont(index):
    return ft.Container(
        height=223,
        width=600,
        content=ft.Row([
            ft.Image(
                src=connection.get_img(index),
                width=225,
                height=225,

            ),
            ft.Column(
                spacing=18,

                controls=[
                    top_text.top_text(index),
                    last_location_text.location(index),
                    fist_seen.first_seen_in(index),
                ],
                alignment=ft.alignment.top_center,
            ),
        ]),

        bgcolor="#383A3F",
        border_radius=ft.border_radius.all(10),
    )
