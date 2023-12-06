# voting_gui.py
import tkinter as tk
from tkinter import messagebox
from voting_functions import VotingAppFunctions

class VotingAppGUI:
    def __init__(self, master: tk.Tk) -> None:
        self.master = master
        self.master.title("Voting App")
        self.master.geometry("400x300")

        # Disable resizing
        self.master.resizable(False, False)

        self.voting_functions = VotingAppFunctions()

        self.create_widgets()

    def create_widgets(self) -> None:
        self.name_label = tk.Label(self.master, text='Your Name:')
        self.name_label.grid(row=0, column=0, pady=5, sticky='e')

        vcmd = (self.master.register(self.voting_functions.validate_name), '%P')

        self.name_entry = tk.Entry(self.master, validate='key', validatecommand=vcmd)
        self.name_entry.grid(row=0, column=1, pady=5, sticky='w')

        self.candidate_menu_label = tk.Label(self.master, text='CANDIDATE MENU')
        self.candidate_menu_label.grid(row=1, column=0, columnspan=2, pady=10, sticky='n')

        self.button1 = tk.Button(self.master, text='Vote for John', command=lambda: self.voting_functions.vote(1, self.name_entry))
        self.button1.grid(row=2, column=0, padx=10, pady=5, sticky='e')

        self.button2 = tk.Button(self.master, text='Vote for Jane', command=lambda: self.voting_functions.vote(2, self.name_entry))
        self.button2.grid(row=2, column=1, padx=10, pady=5, sticky='w')

        self.button3 = tk.Button(self.master, text='Vote for Jack', command=lambda: self.voting_functions.vote(3, self.name_entry))
        self.button3.grid(row=3, column=0, padx=10, pady=5, sticky='e')

        self.button4 = tk.Button(self.master, text='Vote for Jill', command=lambda: self.voting_functions.vote(4, self.name_entry))
        self.button4.grid(row=3, column=1, padx=10, pady=5, sticky='w')

        self.exit_button = tk.Button(self.master, text='Exit', command=self.master.destroy)
        self.exit_button.grid(row=4, column=0, columnspan=2, pady=10, sticky='s')

        # Configure columns and rows to center content
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.master.rowconfigure(2, weight=1)
        self.master.rowconfigure(3, weight=1)
        self.master.rowconfigure(4, weight=1)

def main() -> None:
    try:
        root = tk.Tk()
        app = VotingAppGUI(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

if __name__ == '__main__':
    main()
