import flet as ft

import connection

def first_seen_in(index):
    return ft.Column(
        spacing=0,
        alignment=ft.alignment.bottom_center,
        controls=[
            ft.Text(
                value="First seen in: ",
                size=15,
                color="#5B5C5E",
                weight=ft.FontWeight.W_600
            ),
            ft.Text(
                value=connection.get_first_location(index),
                size=18,
                color="white",
            ),
        ]
    )