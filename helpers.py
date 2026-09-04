import tkinter as tk
import config


def clear_window(root):
    """Destroys active widgets and updates the window background to match the active theme."""
    theme = config.get_theme()
    root.configure(bg=theme["BG_DARK"])
    for widget in root.winfo_children():
        widget.destroy()


def create_card(root, width=420):
    theme = config.get_theme()

    container = tk.Frame(root, bg=theme["BG_DARK"])
    container.pack(expand=True, fill="both")

    card = tk.Frame(
        container,
        bg=theme["CARD_BG"],
        padx=35,
        pady=35,
        highlightbackground=theme["BORDER"],
        highlightthickness=1
    )
    card.place(relx=0.5, rely=0.5, anchor="center")
    return card


def create_button(parent, text, command, type="primary", width=25):
    theme = config.get_theme()

    if type == "primary":
        bg_color, hover_color, fg_color = theme["PRIMARY"], theme["PRIMARY_HOVER"], "#ffffff"
    elif type == "danger":
        bg_color, hover_color, fg_color = theme["DANGER"], theme["DANGER_HOVER"], "#ffffff"
    else:
        bg_color, hover_color, fg_color = theme["SECONDARY"], theme["SECONDARY_HOVER"], theme["TEXT_MAIN"]

    btn = tk.Button(
        parent,
        text=text,
        command=command,
        font=(theme["FONT_FAMILY"], 10, "bold"),
        bg=bg_color,
        fg=fg_color,
        activebackground=hover_color,
        activeforeground=fg_color,
        bd=0,
        relief="flat",
        cursor="hand2",
        width=width,
        pady=8
    )

    btn.bind("<Enter>", lambda e: btn.config(bg=hover_color))
    btn.bind("<Leave>", lambda e: btn.config(bg=bg_color))

    return btn


def create_input(parent, label_text, show=None):
    theme = config.get_theme()

    lbl = tk.Label(
        parent,
        text=label_text,
        font=(theme["FONT_FAMILY"], 9, "bold"),
        fg=theme["TEXT_MUTED"],
        bg=theme["CARD_BG"],
        anchor="w"
    )
    lbl.pack(fill="x", pady=(10, 2))

    entry = tk.Entry(
        parent,
        show=show,
        font=(theme["FONT_FAMILY"], 11),
        bg=theme["INPUT_BG"],
        fg=theme["TEXT_MAIN"],
        insertbackground=theme["TEXT_MAIN"],
        bd=0,
        relief="flat",
        highlightbackground=theme["BORDER"],
        highlightthickness=1
    )
    entry.pack(fill="x", ipady=7, pady=(0, 10))
    return entry


def create_theme_toggle(root, refresh_callback):
    """Creates a top-right button to toggle themes and refresh the view."""
    theme = config.get_theme()

    def on_toggle():
        config.toggle_theme()
        refresh_callback()  # Re-renders the active page with the new colors

    toggle_btn = tk.Button(
        root,
        text=theme["TOGGLE_BTN_TEXT"],
        command=on_toggle,
        font=(theme["FONT_FAMILY"], 9, "bold"),
        bg=theme["CARD_BG"],
        fg=theme["TEXT_MAIN"],
        activebackground=theme["INPUT_BG"],
        activeforeground=theme["TEXT_MAIN"],
        bd=1,
        relief="solid",
        cursor="hand2",
        padx=10,
        pady=4
    )
    # Place in top right corner of root
    toggle_btn.place(relx=0.98, rely=0.03, anchor="ne")

