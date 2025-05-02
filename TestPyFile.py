import tkinter as tk

# Tworzymy główne okno
root = tk.Tk()
root.title("Hello World App")

# Ustawiamy rozmiar okna
root.geometry("300x100")

# Tworzymy etykietę z napisem Hello World
label = tk.Label(root, text="Hello World", font=("Arial", 24))
label.pack(pady=20)  # pady = padding góra-dół

# Uruchamiamy główną pętlę aplikacji
root.mainloop()
