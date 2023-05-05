import tkinter as tk
from tkinter import filedialog, messagebox
from bs4 import BeautifulSoup


def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("HTML Files", "*.html")])

    if not file_path:
        return

    with open(file_path, "r") as file:
        input_html.delete(1.0, tk.END)
        input_html.insert(tk.END, file.read())


def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("HTML Files", "*.html")])

    if not file_path:
        return

    with open(file_path, "w") as file:
        file.write(input_html.get(1.0, tk.END))


def clean_html():
    try:
        soup = BeautifulSoup(input_html.get(1.0, tk.END), "html.parser")
        clean_code = soup.prettify()
        input_html.delete(1.0, tk.END)
        input_html.insert(tk.END, clean_code)
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al limpiar el HTML: {e}")


root = tk.Tk()
root.title("Herramienta Clean HTML")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

input_html = tk.Text(frame, wrap=tk.NONE, undo=True)
input_html.pack(expand=True, fill=tk.BOTH)

scrollbar_x = tk.Scrollbar(frame, orient=tk.HORIZONTAL, command=input_html.xview)
scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

scrollbar_y = tk.Scrollbar(frame, orient=tk.VERTICAL, command=input_html.yview)
scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

input_html.config(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="Archivo", menu=file_menu)
file_menu.add_command(label="Abrir", command=open_file)
file_menu.add_command(label="Guardar como", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Salir", command=root.quit)

tools_menu = tk.Menu(menu)
menu.add_cascade(label="Herramientas", menu=tools_menu)
tools_menu.add_command(label="Limpiar HTML", command=clean_html)

root.mainloop()
