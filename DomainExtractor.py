"""
Python script to extract domain from a long URL.
"""

import tkinter as tk
from urllib.parse import urlparse
import pyperclip

def extract_domain():
    url = url_entry.get()
    try:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        if domain.startswith('www.'):
            domain = domain[4:]
        result_label.config(text=f"Domain: {domain}")
        copy_button.config(state='normal', command=lambda: pyperclip.copy(domain))
    except:
        result_label.config(text="Invalid URL")
        copy_button.config(state='disabled')

# Create main window
root = tk.Tk()
root.title("URL Domain Extractor")
root.geometry("400x200")

# Create and pack widgets
tk.Label(root, text="Paste URL:").pack(pady=10)
url_entry = tk.Entry(root, width=40)
url_entry.pack(pady=5)

extract_button = tk.Button(root, text="Extract Domain", command=extract_domain)
extract_button.pack(pady=10)

result_label = tk.Label(root, text="Domain: ")
result_label.pack(pady=10)

copy_button = tk.Button(root, text="Copy Domain", state='disabled')
copy_button.pack(pady=5)

# Start the main loop
root.mainloop()