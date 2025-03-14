import tkinter as tk
from tkinter import ttk, messagebox
import ClassicMeth.PlayFaire as pf
import ClassicMeth.Vigenere as vg
import ClassicMeth.TranspositionCol as tc
class UserInterface:
    def __init__(self, master):
        self.master = master
        self.master.title("CryptoX")
        self.master.geometry("800x400")
        # Right div
        self.main_right = tk.Frame(window, width=400, height=400, bg="#949EFF")
        # Left div
        self.main_left = tk.Frame(window, width=400, height=400, bg="#fff")
        self.main_right.pack(side=tk.RIGHT)
        self.main_left.pack(side=tk.LEFT)
        # Main Header h1
        self.header = tk.Label(self.main_left,
                  text="Welcome to CryptoX \n Start Encrypting \nby Choosing a Method",
                  fg="#949EFF",
                  bg="#fff",
                  font=("Helvetica", "24", "bold"), padx=10, pady=10)
        self.header.place(x=1)

        # Select Label (Text)
        self.method_selection = tk.Label(self.main_left,
                            text="Select Method:",
                            bg="#fff",
                            font=("Arial", "16", "bold"))
        self.method_selection.place(y=150)

        # Drop Down Menu to Select the Encrypting Method
        self.drop_down = ttk.Combobox(self.main_left, values=["Playfaire", "Vigenère", "Transposition Colonne"])
        self.drop_down.place(x=180, y=155)

        # Key Label
        self.label_key = tk.Label(self.main_right, text="Enter Key:", bg="#949EFF",fg="#fff",font=("Helvetica", "16", "bold"))
        self.label_key.place(x=0, y=30)
        # Key Input
        self.input_key = tk.Entry(self.main_right, width=30)
        self.input_key.place(x=120, y=35)

        # Text Label
        self.label_data = tk.Label(self.main_right, text="Enter Data:", bg="#949EFF",fg="#fff",font=("Helvetica", "16", "bold"))
        self.label_data.place(x=0, y=60)
        # Key Input
        self.input_data = tk.Text(self.main_right, height=5, width=30)
        self.input_data.place(x=120, y=70)

        # Switching Between Encrypt And Decrypt
        self.decrypt_var = tk.BooleanVar()
        self.checkbox_decrypt = tk.Checkbutton(self.main_right, text="Decrypt",bg="#949EFF", font=("Helvetica", "8", "bold"), variable=self.decrypt_var)
        self.checkbox_decrypt.place(x=0, y=10)
        
        execute_button = tk.Button(self.main_right, text="Perform Action", command=self.execute)
        execute_button.place(x=20, y= 250)

    def execute(self):
        method = self.drop_down.get()
        key = self.input_key.get()
        data = self.input_data.get("1.0", tk.END).strip()
        result = None

        if self.decrypt_var.get():
            if method == "Playfaire":
                methodClass = pf.PlayfairCipher(key, data)
                result = methodClass.playfaireDecrypt()
                print()
            elif method == "Vigenère":
                methodClass = vg.VigenereCipher(key, data)
                print()
                methodClass.vigenereCipherDecrypt()
            elif method == "Transposition Colonne":
                methodClass = tc.TranspositionColonne(key, data)
                result= methodClass.transpositionColonneDecrypt()
        
        else:
            if method == "Playfaire":
                methodClass = pf.PlayfairCipher(key, data)
                result = methodClass.playfaireEncrypt()
            elif method == "Vigenère":
                methodClass = vg.VigenereCipher(key, data)
                result = methodClass.vigenereCipherEncrypt()
            elif method == "Transposition Colonne":
                methodClass = tc.TranspositionColonne(key, data)
                result = methodClass.transpositionColonneEncrypt()
        if result is not None:
            messagebox.showinfo("Result", result)
        else:
            messagebox.showerror("Error", "Please select a valid method and enter the necessary data.")

window = tk.Tk()
UserInterface(window)
window.mainloop()