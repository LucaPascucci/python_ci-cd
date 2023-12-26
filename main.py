import tkinter as tk

def somma_numeri():
    try:
        numero1 = float(entry_numero1.get())
        numero2 = float(entry_numero2.get())
        risultato.set(f"La somma è: {numero1 + numero2}")
    except ValueError:
        risultato.set("Inserisci numeri validi")

# Creazione della finestra principale
root = tk.Tk()
root.title("Calcolatrice Somma")

# Variabili di controllo per i widget
risultato = tk.StringVar()

# Etichetta e campo di input per il primo numero
tk.Label(root, text="Primo Numero:").grid(row=0, column=0)
entry_numero1 = tk.Entry(root)
entry_numero1.grid(row=0, column=1)

# Etichetta e campo di input per il secondo numero
tk.Label(root, text="Secondo Numero:").grid(row=1, column=0)
entry_numero2 = tk.Entry(root)
entry_numero2.grid(row=1, column=1)

# Pulsante per eseguire la somma
tk.Button(root, text="Somma", command=somma_numeri).grid(row=2, column=0, columnspan=2)

# Casella di testo per visualizzare il risultato
tk.Label(root, textvariable=risultato).grid(row=3, column=0, columnspan=2)

# Avvia il loop principale della GUI
root.mainloop()
