import os
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import filedialog, messagebox

def translate_with_google_translate(text, source_lang, target_lang):
    url = f'https://translate.google.com/m?hl={target_lang}&sl={source_lang}&q={text}'
    
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        translation = soup.find('div', {'class': 'result-container'}).text.strip()
        return translation
    else:
        return f"Translation request failed with status code: {response.status_code}"

def translate_and_save_to_user_path():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    source_language = source_language_entry.get()
    
    if not file_path:
        return
    
    save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    
    if not save_path:
        return
    
    with open(file_path, 'r', encoding='utf-8') as input_file:
        with open(save_path, 'w', encoding='utf-8') as translated_file:
            for line in input_file:
                line = line.strip()
                if line:
                    translated_line = translate_with_google_translate(line, source_language, "en")
                    translated_file.write(translated_line + '\n')
    
    messagebox.showinfo("Success", f"Translation saved to '{save_path}'.")
    messagebox.showinfo("File Uploaded", "File Uploaded")

app = tk.Tk()
app.title("Text Translator")

# Set up the style
style = ttk.Style(app)
style.configure('TLabel', font=('Arial', 12), padding=10, background='black', foreground='white')
style.configure('TEntry', font=('Arial', 12), padding=10, fieldbackground='black', foreground='white')
style.configure('TFrame', background='black')

# Create a frame for padding and background color
frame = tk.Frame(app, relief="sunken", borderwidth=5, bg='black')
frame.pack(fill='both', expand=True, padx=20, pady=20)

# Upload button
upload_button = tk.Button(frame, text="Upload Text File", command=translate_and_save_to_user_path, font=('Arial', 12), bg='red', fg='white', activebackground='darkred', activeforeground='white')
upload_button.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

# Source language label
source_language_label = tk.Label(frame, text="Enter Source Language Code:", font=('Arial', 12), bg='black', fg='white')
source_language_label.grid(row=1, column=0, pady=10, sticky='e')

# Source language entry
source_language_entry = tk.Entry(frame, width=10, font=('Arial', 12), bg='black', fg='white', insertbackground='white')
source_language_entry.grid(row=1, column=1, pady=10, sticky='w')
source_language_entry.insert(0, "kn")

# Translate and save button
translate_button = tk.Button(frame, text="Translate and Save", command=translate_and_save_to_user_path, font=('Arial', 12), bg='red', fg='white', activebackground='darkred', activeforeground='white')
translate_button.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

# Center the window on the screen
app.update_idletasks()
width = app.winfo_width()
height = app.winfo_height()
x = (app.winfo_screenwidth() // 2) - (width // 2)
y = (app.winfo_screenheight() // 2) - (height // 2)
app.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# Set the background color of the main window
app.configure(bg='black')

app.mainloop()
