import tkinter as tk
from tkinter import ttk

# Create the main application window
root = tk.Tk()
root.title("Tabbed Application")

# Create a notebook (tabbed interface)
notebook = ttk.Notebook(root)

# Create three tab frames
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)

# Add tabs to the notebook
notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.add(tab3, text="Tab 3")

# Customize the tab appearance if desired
style = ttk.Style()
style.configure("TNotebook", tabposition="wn")  # Change tab position (optional)

# Place the notebook in the main window
notebook.pack(expand=True, fill="both")

# Add widgets to each tab
label1 = ttk.Label(tab1, text="This is Tab 1")
label1.pack(padx=20, pady=20)

label2 = ttk.Label(tab2, text="This is Tab 2")
label2.pack(padx=20, pady=20)

label3 = ttk.Label(tab3, text="This is Tab 3")
label3.pack(padx=20, pady=20)

# Start the Tkinter event loop
root.mainloop()