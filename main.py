import flet as ft

import conteiner_info

def main(page):
    page.title = "Rick and Morty"
    page.background = "white"
    page.scroll = "adaptive"
    page.padding = 0

    cont = ft.Container(
        bgcolor="#202329",
        width=1920,
        padding=ft.padding.only(top=30, left=20, right=20, bottom=15),
        content=ft.Row(
            wrap=True,
            spacing=22,
            controls=[
                conteiner_info.cont(0),
                conteiner_info.cont(1),
                conteiner_info.cont(9),
                conteiner_info.cont(12),
                conteiner_info.cont(16),
                conteiner_info.cont(19),
            ],

        )
    )


    page.add(cont)
ft.app(target=main)