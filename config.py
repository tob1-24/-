# ==========================
# GLOBAL CONFIG & DATA
# ==========================

users = {}

LOCATIONS = {
    "Africa": {
        "Lagos": (6.5244, 3.3792),
        "Accra": (5.6037, -0.1870),
        "Johannesburg": (-26.2041, 28.0473)
    },
    "Europe": {
        "London": (51.5074, -0.1278),
        "Paris": (48.8566, 2.3522),
        "Berlin": (52.5200, 13.4050)
    },
    "Asia": {
        "Tokyo": (35.6762, 139.6503),
        "Beijing": (39.9042, 116.4074),
        "Dubai": (25.2048, 55.2708)
    },
    "North America": {
        "New York": (40.7128, -74.0060),
        "Toronto": (43.6532, -79.3832),
        "Mexico City": (19.4326, -99.1332)
    },
    "South America": {
        "Rio": (-22.9068, -43.1729),
        "Santiago": (-33.4489, -70.6693),
        "Buenos Aires": (-34.6037, -58.3816)
    }
}

# ==========================
# THEMES
# ==========================

DARK_THEME = {
    "NAME": "dark",
    "BG_DARK": "#0f172a",        # Dark Slate
    "CARD_BG": "#1e293b",
    "INPUT_BG": "#334155",
    "TEXT_MAIN": "#f8fafc",
    "TEXT_MUTED": "#94a3b8",
    "BORDER": "#334155",
    "PRIMARY": "#3b82f6",
    "PRIMARY_HOVER": "#2563eb",
    "SECONDARY": "#475569",
    "SECONDARY_HOVER": "#334155",
    "DANGER": "#ef4444",
    "DANGER_HOVER": "#dc2626",
    "TOGGLE_BTN_TEXT": "☀️ Light Mode",
    "FONT_FAMILY": "Segoe UI"
}

LIGHT_THEME = {
    "NAME": "light",
    "BG_DARK": "#f8fafc",        # Bright Off-White
    "CARD_BG": "#ffffff",
    "INPUT_BG": "#f1f5f9",
    "TEXT_MAIN": "#0f172a",
    "TEXT_MUTED": "#64748b",
    "BORDER": "#e2e8f0",
    "PRIMARY": "#2563eb",
    "PRIMARY_HOVER": "#1d4ed8",
    "SECONDARY": "#cbd5e1",
    "SECONDARY_HOVER": "#94a3b8",
    "DANGER": "#ef4444",
    "DANGER_HOVER": "#dc2626",
    "TOGGLE_BTN_TEXT": "🌙 Dark Mode",
    "FONT_FAMILY": "Segoe UI"
}

# Active Theme State
current_theme_name = "dark"

def get_theme():
    """Returns the current active theme dictionary."""
    return DARK_THEME if current_theme_name == "dark" else LIGHT_THEME

def toggle_theme():
    """Switches the theme back and forth."""
    global current_theme_name
    current_theme_name = "light" if current_theme_name == "dark" else "dark"
