import os
import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy.editor import VideoFileClip
from PIL import Image

def convert_files():
    source_folder = folder_path.get()
    convert_to_mp4 = var_mp4.get()
    convert_to_webm = var_webm.get()
    convert_to_png = var_png.get()
    delete_gif = var_delete.get()

    if not source_folder:
        messagebox.showerror("Errore", "Seleziona una cartella")
        return

    for file in os.listdir(source_folder):
        if file.endswith('.gif'):
            file_path = os.path.join(source_folder, file)
            base_name = os.path.splitext(file)[0]

            if convert_to_mp4:
                mp4_folder = os.path.join(source_folder, "mp4")
                os.makedirs(mp4_folder, exist_ok=True)
                video = VideoFileClip(file_path)
                video.write_videofile(os.path.join(mp4_folder, base_name + '.mp4'), codec='libx264', fps=30)

            if convert_to_webm:
                webm_folder = os.path.join(source_folder, "webm")
                os.makedirs(webm_folder, exist_ok=True)
                video = VideoFileClip(file_path)
                video.write_videofile(os.path.join(webm_folder, base_name + '.webm'), codec='libvpx', fps=30)

            if convert_to_png:
                png_folder = os.path.join(source_folder, "png")
                os.makedirs(png_folder, exist_ok=True)
                with Image.open(file_path) as img:
                    img.save(os.path.join(png_folder, base_name + '.png'))

            if delete_gif:
                os.remove(file_path)

    messagebox.showinfo("Completato", "Conversione completata")

app = tk.Tk()
app.title("Convertitore di GIF")

folder_path = tk.StringVar()

def browse_folder():
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)

# Variabili per le opzioni di conversione
var_mp4 = tk.BooleanVar()
var_webm = tk.BooleanVar()
var_png = tk.BooleanVar()
var_delete = tk.BooleanVar()

# Layout
tk.Label(app, text="Seleziona la cartella dei GIF:").pack()
tk.Entry(app, textvariable=folder_path, width=50).pack()
tk.Button(app, text="Sfoglia", command=browse_folder).pack()
tk.Checkbutton(app, text="Converti in MP4", variable=var_mp4).pack()
tk.Checkbutton(app, text="Converti in WebM", variable=var_webm).pack()
tk.Checkbutton(app, text="Converti in PNG", variable=var_png).pack()
tk.Checkbutton(app, text="Elimina i GIF originali", variable=var_delete).pack()
tk.Button(app, text="Converti", command=convert_files).pack()

app.mainloop()
