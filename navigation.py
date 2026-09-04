import tkinter as tk

from darkdetect import theme
from tkintermapview import TkinterMapView
import config
import helpers
import auth

def show_continents(root):
    helpers.clear_window(root)
    theme= config.get_theme()
    helpers.create_theme_toggle(root, lambda: show_continents(root))
    card = helpers.create_card(root, width=480)

    tk.Label(
        card,
        text= "SELECT A CONTINENT",
        font=(theme["FONT_FAMILY"], 20, "bold"),
        fg= theme["TEXT_MAIN"],
        bg= theme["CARD_BG"]
    ).pack(pady=(0,15))

    #Button to show our ciazties
    for continent in config.LOCATIONS.keys():
        btn= helpers.create_button(
            card,
            continent,
            lambda c=continent: show_cities(root, c),
            type= "secondary",
            width=28
          )
        btn.pack(pady=4)

    helpers.create_button(
        card,
        "Sign Out",
        lambda: auth.show_login(root),
        type="danger",
        width=28
    ).pack(pady=(20,0))



#function to show cities

def show_cities(root, continent):
    helpers.clear_window(root)
    theme= config.get_theme()

    helpers.create_theme_toggle(root, lambda: show_cities(root, continent))

    card= helpers.create_card(root, width=480)
    tk.Label(
        card,
        text=f"{continent} Destinations",
        font=(theme["FONT_FAMILY"], 20, "bold"),
        fg=theme["TEXT_MAIN"],
        bg=theme["CARD_BG"]
    ).pack(pady=(0,15))

    cities= config.LOCATIONS[continent]


    for city in cities.keys():
        btn= helpers.create_button(
            card,
            f"{city}",
            lambda c=city: open_map(root, continent, c),
            type="primary",
            width=28,
        )
        btn.pack(pady=4)

    helpers.create_button(
        card,
        "Back to continents",

        lambda:show_continents(root),
        type="secondary",
        width=28
    ).pack(pady=(20,0))

 #Function to open map
def open_map(root, continent, city):
    helpers.clear_window(root)
    theme= config.get_theme()
    lat, lon= config.LOCATIONS[continent][city]

    #Top navigationbar
    top_bar=tk.Frame(root,bg=theme["CARD_BG"], pady=12, padx=20)
    top_bar.pack(side="top", fill="x")
#City title
    tk.Label(
        top_bar,
        text=f"{city}, {continent}",
        font=(theme["FONT_FAMILY"], 16, "bold"),
        fg=theme["TEXT_MAIN"],
        bg=theme["CARD_BG"]
    ).pack(side="left")

   # title.pack(side= "left")
    helpers.create_button(
        top_bar,
        "Home",
        lambda: show_continents(root),
        type= "secondary",
        width=8

    ).pack(side="right", padx=4)

    helpers.create_button(
        top_bar,
        "Back",
        lambda: show_cities(root, continent),
        type="primary",
        width=8
    ).pack(side="right", padx=4)

    def toggle_map_theme():
        config.toggle_theme()
        open_map(root, continent, city)

    tk.Button(
        top_bar,
        text=theme["TOGGLE_BTN_TEXT"],
        command=toggle_map_theme,
        font=(theme["FONT_FAMILY"], 9, "bold"),
        bg= theme["INPUT_BG"],
        fg= theme["TEXT_MAIN"],
        bd=0,
        relief="flat",
        cursor="hand2",
        padx=8,
        pady=5
    ).pack(side="right", padx=10)

    #Map Display
    # map_widget= TkinterMapView(root, width=1000, height=550)
    map_widget = TkinterMapView(root)
    map_widget.pack(fill="both", expand=True)

    map_widget.set_position(lat, lon)
    map_widget.set_zoom(11)
    map_widget.set_marker(lat, lon, text=city)
