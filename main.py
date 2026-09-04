import tkinter as tk
import config
import auth

def main():
    root = tk.Tk()
    root.title("World Explorer")
    root.geometry("1000x650")

    # Set initial background color based on active theme
    theme = config.get_theme()
    root.configure(bg=theme["BG_DARK"])

    # Launch authentication flow
    auth.show_login(root)

    # Start application event loop
    root.mainloop()

if __name__ == "__main__":
    main()
