from tkinter import *  
from tkinter import ttk

def transcrire_ascii(): 
    input_text = entry.get()
    ascii_text = [str(ord(char)) for char in input_text]
    result_label.config(text="ASCII : " + " ".join(ascii_text))

def transcrire_texte():
    input_numbers = entry_ascii.get()
    try:
        # Évaluation de la chaîne pour transformer l'entrée en une liste de nombres
        ascii_values = eval(input_numbers)  # On utilise eval pour interpréter la liste comme entrée
        if isinstance(ascii_values, list) and all(isinstance(num, int) for num in ascii_values):
            text = "".join([chr(num) for num in ascii_values])
            result_label2.config(text="Texte : " + text)
        else:
            result_label2.config(text="Erreur : Veuillez entrer une liste de nombres valides")
    except (ValueError, SyntaxError):
        result_label2.config(text="Erreur : Format de liste non valide")

root = Tk()
root.title("Transcripteur ASCII et Texte")

# Création des éléments pour la transcription texte en ASCII
entry_label = ttk.Label(root, text="Entrez une phrase :")
entry = ttk.Entry(root, width=50)
button_ascii = ttk.Button(root, text="Transcrire en ASCII", command=transcrire_ascii)
result_label = ttk.Label(root, text="ASCII :")

# Création des éléments pour la transcription ASCII en texte
entry_label_ascii = ttk.Label(root, text="Entrez une liste de nombres ASCII :")
entry_ascii = ttk.Entry(root, width=50)
button_text = ttk.Button(root, text="Transcrire en Texte", command=transcrire_texte)
result_label2 = ttk.Label(root, text="Texte :")

# Placement des éléments dans la fenêtre
entry_label.grid(row=0, column=0, padx=10, pady=10)
entry.grid(row=0, column=1, padx=10, pady=10)
button_ascii.grid(row=1, column=1, padx=10, pady=10)
result_label.grid(row=2, column=1, padx=10, pady=10)

entry_label_ascii.grid(row=3, column=0, padx=10, pady=10)
entry_ascii.grid(row=3, column=1, padx=10, pady=10)
button_text.grid(row=4, column=1, padx=10, pady=10)
result_label2.grid(row=5, column=1, padx=10, pady=10)

root.mainloop()
