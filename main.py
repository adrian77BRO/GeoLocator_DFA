import tkinter as tk
from gui import create_gui

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Validador de coordenadas")
    window.geometry("700x600")
    window.configure(bg='#69f5ad')
    
    create_gui(window)
    
    window.mainloop()