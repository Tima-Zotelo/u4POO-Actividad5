import tkinter as tk
import json
from urllib.request import urlopen

API_KEY = "dd124937eff252f24cbf1b59475d17c3"

root = tk.Tk()
root.title("Cinéfilos Argentinos")

movie_listbox = tk.Listbox(root)
movie_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


movie_frame = tk.Frame(root)
movie_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

def show_movie_details(event):
    selection = movie_listbox.curselection()
    title = movie_listbox.get(selection)

    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={title}"
    response = urlopen (url)
    data = json.loads(response.read())

    # Mostrar los detalles de la película en el frame
    for widget in movie_frame.winfo_children():
        widget.destroy()
    tk.Label(movie_frame, text=data["title"]).pack()
    tk.Label(movie_frame, text=data["overview"]).pack()
    tk.Label(movie_frame, text=data["original_language"]).pack()
    tk.Label(movie_frame, text=data["release_date"]).pack()
    genres = ", ".join([genre["name"] for genre in data["genre_ids"]])
    tk.Label(movie_frame, text=genres).pack()

# obtener peliculas
url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}"
response = urlopen (url)
data = json.loads(response.read())

# Agregar los títulos de las películas al listbox
for movie in data:
    movie_listbox.insert(tk.END, movie["title"])

# Asociar la función a la acción de hacer doble click en un título de película
movie_listbox.bind("<Double-Button-1>", show_movie_details)

# Iniciar la aplicación
root.mainloop()
