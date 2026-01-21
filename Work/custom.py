import tkinter as tk
from tkinter import ttk

def get_input():
    user_input = entry_widget.get()
    selected_option = combo_box.get()
    print("User entered:", user_input)
    print("Selected option:", selected_option)
    # You can perform further actions with user_input and selected_option here

root = tk.Tk()
root.title("User Input Example")

# Set futuristic black theme colors
bg_color = "#121212"  # Very dark gray/black background
fg_color = "#00FFCF"  # Bright cyan/teal text for a futuristic vibe
entry_bg = "#1E1E1E"  # Dark gray for entry background
button_bg = "#00B894"  # Slightly darker teal for button background
button_fg = "#121212"  # Dark text color for button text
combo_bg = "#1E1E1E"  # Dark background for combobox
combo_fg = fg_color

root.configure(bg=bg_color)

# Create a Label to prompt the user
label = tk.Label(root, text="Enter something:", bg=bg_color, fg=fg_color, font=("Segoe UI", 12, "bold"))
label.pack(pady=5)

# Create the Entry widget
entry_widget = tk.Entry(root, width=40, bg=entry_bg, fg=fg_color, insertbackground=fg_color, font=("Segoe UI", 12))
entry_widget.pack(pady=10)

# Create a drop box (Combobox) with list FF, VS, LKP
combo_box = ttk.Combobox(root, values=["FF", "VS", "LKP"], font=("Segoe UI", 12))
combo_box.pack(pady=10)
combo_box.set("Select an option")

# Style ttk Combobox for dark theme
style = ttk.Style()
style.theme_use('clam')
style.configure("TCombobox",
                fieldbackground=combo_bg,
                background=combo_bg,
                foreground=combo_fg,
                arrowcolor=fg_color,
                font=("Segoe UI", 12, "bold"))

# Create a Button to trigger input retrieval
submit_button = tk.Button(root, text="Get Input", command=get_input, bg=button_bg, fg=button_fg, activebackground="#00FFC8", font=("Segoe UI", 12, "bold"))
submit_button.pack(pady=5)

root.mainloop()
