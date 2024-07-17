import flet as ft
import sqlite3

def main(page: ft.Page):
    page.title = "SQL Test"

    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT * FROM customers")
    items = c.fetchall()

    page.add(ft.Text("Show Data", size=15, color=ft.colors.BLACK))

    for item in items:
        page.add(
            ft.Text(item, size=20, color=ft.colors.ORANGE)
        )

    conn.commit()
    conn.close()


ft.app(main)
