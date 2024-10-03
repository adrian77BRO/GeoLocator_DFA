import tkinter as tk
import csv
from tkinter import ttk, filedialog, messagebox
from coordinates_DFA import extract_coordinates_from_text
from file_handler import extract_text_from_docx,extract_text_from_pdf, clean_pdf_text, extract_text_from_html

valid_coords = []

def open_file():
    global valid_coords
    file_path = filedialog.askopenfilename(filetypes=[
        ("Text files", "*.txt"), 
        ("Word files", "*.docx"), 
        ("PDF files", "*.pdf"), 
        ("HTML files", "*.html")])
    
    if file_path:
        text = ""
        if file_path.endswith('.txt'):
            with open(file_path, 'r', encoding="utf-8") as file:
                text = file.read()
        elif file_path.endswith('.docx'):
            text = extract_text_from_docx(file_path)
        elif file_path.endswith('.pdf'):
            text = extract_text_from_pdf(file_path)
            text = clean_pdf_text(text)
        elif file_path.endswith('.html'):
            text = extract_text_from_html(file_path)

        valid_coords = extract_coordinates_from_text(text)
        if valid_coords:
            table.delete(*table.get_children())
            for coord, fila, posicion in valid_coords:
                table.insert("", "end", values=(coord, fila, posicion))
        else:
            messagebox.showinfo("Resultado", "No se encontraron coordenadas válidas.")

def save_coordinates_to_csv(coordinates, output_file):
    headers = ["Coordenadas", "Fila", "Posición"]

    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for coord in coordinates:
            writer.writerow([coord[0], coord[1], coord[2]])

    messagebox.showinfo("Éxito", f"Coordenadas guardadas en {output_file}")

def save_file():
    if not valid_coords:
        messagebox.showwarning("Advertencia", "No hay coordenadas para guardar.")
        return
    
    output_file = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if output_file:
        save_coordinates_to_csv(valid_coords, output_file)

def create_gui(window):
    frame = tk.Frame(window, bg='#69f5ad')
    frame.place(relx=0.5, rely=0.2, anchor="center")

    label = tk.Label(frame, text="Seleccione un archivo para extraer coordenadas válidas", font=("Comic Sans MS", 14), bg='#69f5ad')
    label.pack(pady=10)

    button_frame = tk.Frame(frame, bg='#69f5ad')
    button_frame.pack(pady=10)

    open_button = tk.Button(button_frame, text="Abrir archivo", font=("Comic Sans MS", 12), bg='#007BFF', fg='white', command=open_file)
    open_button.pack(side="left", padx=10)

    save_button = tk.Button(button_frame, text="Guardar en Excel", font=("Comic Sans MS", 12), bg='#28a745', fg='white', command=save_file)
    save_button.pack(side="left", padx=10)

    table_frame = tk.Frame(window, bg='#69f5ad')
    table_frame.place(relx=0.5, rely=0.6, anchor="center")

    style = ttk.Style()
    style.configure("Treeview", background="#7ae7fa", foreground="black", fieldbackground="#7ae7fa", font=("Comic Sans MS", 12), rowheight=25)
    style.configure("Treeview.Heading", font=("Comic Sans MS", 12, "bold"), background="#7ae7fa", foreground="black")

    columns = ("Coordenadas", "Fila", "Posición")
    global table
    table = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)
    table.heading("Coordenadas", text="Coordenadas válidas")
    table.heading("Fila", text="Fila")
    table.heading("Posición", text="Posición")

    table.column("Coordenadas", minwidth=200, width=300, anchor="center")
    table.column("Fila", minwidth=50, width=100, anchor="center")
    table.column("Posición", minwidth=50, width=100, anchor="center")
    table.pack(pady=20)

    scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
    scrollbar.pack(side="right", fill="y")
    table.configure(yscrollcommand=scrollbar.set)