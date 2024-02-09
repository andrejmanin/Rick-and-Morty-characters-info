import flet as ft
import connection

def icon(is_dead):
    if is_dead == "Dead":
        return ft.Icon(
            name=ft.icons.RADIO_BUTTON_CHECKED,
            size=18,
            color="red"
        )
    else:
        return ft.Icon(
            name=ft.icons.RADIO_BUTTON_CHECKED,
            size=18,
            color="green"
        )

def top_text(index):
    return ft.Column(
        spacing=0,
        alignment=ft.alignment.top_center,
        controls=[
            ft.Text(
                value=connection.get_name(index),
                size=25,
                color="white",
                weight=ft.FontWeight.W_900,
                selectable=True
            ),
            ft.Row(
                spacing=1,
                controls=[
                    icon(connection.get_status(index)),
                    ft.Text(

                        value=connection.get_status(index) + " - " + connection.get_species(index),
                        color="white",
                        text_align=ft.alignment.top_center,
                        size=16,
                        weight=ft.FontWeight.W_600,
                        selectable=True
                    ),

                ]
            )
        ]
    )