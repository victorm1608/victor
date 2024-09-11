import flet as ft
from setuptools import sic


def main(page: ft.Page):
    page.title="¿ayudame por favor?"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.bgcolor="orange"
    
    lbl1=ft.text("¿ayudame por favor",
                Style=ft.TextStyle(size=40,weight="bold"))
    
    src=https://www.informador.mx/__export/1659379855682/sites/elinformador/img/2022/08/01/20160426_crop1659375778693.jpg_423682103.jpg
    
    btnSi=ft.ElevatedButton("Si"
                            color=purple,
                            width=100,
                            height=50
                            )
    btnNo=ft.ElevatedButton("No"
                            color=red,
                            width=100,
                            height=50
                            )
    def no(e):
        btnSi.width+=50
        btnNo.height+=30
        page.update()
        
    def no(e):
        imgi.src="feliz.png"
        page.update()
        
    btnNo.on_click=no
    btnSi.on_click=no+
    
    



ft.app(main)
