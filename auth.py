import tkinter as tk
from tkinter import messagebox
import config
import helpers
import navigation


def show_login(root):
    helpers.clear_window(root)
    theme = config.get_theme()

    # Theme Switcher Button
    helpers.create_theme_toggle(root, lambda: show_login(root))

    card = helpers.create_card(root)

    tk.Label(
        card,
        text="World Explorer",
        font=(theme["FONT_FAMILY"], 22, "bold"),
        fg=theme["TEXT_MAIN"],
        bg=theme["CARD_BG"]
    ).pack(pady=(0, 2))

    tk.Label(
        card,
        text="Sign in to start exploring",
        font=(theme["FONT_FAMILY"], 10),
        fg=theme["TEXT_MUTED"],
        bg=theme["CARD_BG"]
    ).pack(pady=(0, 15))

    username_entry = helpers.create_input(card, "USERNAME")
    password_entry = helpers.create_input(card, "PASSWORD", show="*")

    def login():
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        if username in config.users and config.users[username] == password:
            messagebox.showinfo("Success", f"Welcome back, {username}!")
            navigation.show_continents(root)
        else:
            messagebox.showerror("Error", "Invalid username or password")

    helpers.create_button(card, "Sign In", login, type="primary").pack(pady=(15, 8))
    helpers.create_button(card, "Create Account", lambda: show_register(root), type="secondary").pack()


def show_register(root):
    helpers.clear_window(root)
    theme = config.get_theme()

    helpers.create_theme_toggle(root, lambda: show_register(root))

    card = helpers.create_card(root)

    tk.Label(
        card,
        text="Create Account",
        font=(theme["FONT_FAMILY"], 20, "bold"),
        fg=theme["TEXT_MAIN"],
        bg=theme["CARD_BG"]
    ).pack(pady=(0, 2))

    tk.Label(
        card,
        text="Register your credentials below",
        font=(theme["FONT_FAMILY"], 10),
        fg=theme["TEXT_MUTED"],
        bg=theme["CARD_BG"]
    ).pack(pady=(0, 15))

    username_entry = helpers.create_input(card, "NEW USERNAME")
    password_entry = helpers.create_input(card, "NEW PASSWORD", show="*")

    def register():
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        if not username or not password:
            messagebox.showerror("Error", "All fields are required")
            return

        if username in config.users:
            messagebox.showerror("Error", "Username is already taken")
            return

        config.users[username] = password
        messagebox.showinfo("Success", "Account created successfully!")
        show_login(root)

    helpers.create_button(card, "Register Now", register, type="primary").pack(pady=(15, 8))
    helpers.create_button(card, "Back to Sign In", lambda: show_login(root), type="secondary").pack()
