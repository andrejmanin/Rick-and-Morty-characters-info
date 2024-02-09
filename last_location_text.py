import flet as ft

import connection

def location(index):
    return ft.Column(
        alignment=ft.alignment.center,
        spacing=0,
        controls=[
            ft.Text(
                value="Last known location: ",
                size= 15,
                color="#5B5C5E",
                weight=ft.FontWeight.W_600
            ),
            ft.Text(
                value=connection.get_last_location(index),
                size=18,
                color="white",
            )
        ]
    )