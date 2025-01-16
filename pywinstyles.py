import ctypes
import sys
import sv_ttk as sv_ttk

def change_header_color(root, color):
    # Convert the hex color to RGB
    color = color.lstrip('#')
    rgb = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
    rgb_color = (rgb[2] << 16) | (rgb[1] << 8) | rgb[0]

    hwnd = ctypes.windll.user32.GetParent(root.winfo_id())
    DWMWA_CAPTION_COLOR = 35
    DWMWA_TEXT_COLOR = 36

    # Set the title bar color
    ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd, DWMWA_CAPTION_COLOR, ctypes.byref(ctypes.c_int(rgb_color)), ctypes.sizeof(ctypes.c_int))
    # Set the title bar text color
    ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd, DWMWA_TEXT_COLOR, ctypes.byref(ctypes.c_int(0xFFFFFF if rgb_color < 0x7F7F7F else 0x000000)), ctypes.sizeof(ctypes.c_int))

def apply_style(root, style):
    # Example implementation to apply a style
    # This is a placeholder function and may need to be adjusted based on your requirements
    pass

def apply_theme_to_titlebar(root):
    version = sys.getwindowsversion()

    if version.major == 10 and version.build >= 22000:
        # Set the title bar color to the background color on Windows 11 for better appearance
        change_header_color(root, "#1c1c1c" if sv_ttk.get_theme() == "dark" else "#fafafa")
    elif version.major == 10:
        apply_style(root, "dark" if sv_ttk.get_theme() == "dark" else "normal")

        # A hacky way to update the title bar's color on Windows 10 (it doesn't update instantly like on Windows 11)
        root.wm_attributes("-alpha", 0.99)
        root.wm_attributes("-alpha", 1)