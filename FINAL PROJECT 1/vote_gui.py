import tkinter as tk
from tkinter import messagebox
from voting_functions import VotingAppFunctions
from typing import Any

class VotingAppGUI:
    """
    Class for the graphical user interface of the voting app.
    """
    def __init__(self, master: tk.Tk, voting_functions: VotingAppFunctions) -> None:
        """
        Initialize the VotingAppGUI.

        Parameters:
            master (tk.Tk): The root Tkinter window.
            voting_functions (VotingAppFunctions): Instance of VotingAppFunctions for handling voting logic.
        """
        self.master = master
        self.master.title("Voting App")
        self.master.geometry("400x300")

        # Disable resizing
        self.master.resizable(False, False)

        self.voting_functions = voting_functions

        self.create_widgets()

    def create_widgets(self) -> None:
        """
        Create the GUI widgets for the VotingApp.
        """
        self.name_label = tk.Label(self.master, text='Your Name:')
        self.name_label.grid(row=0, column=0, pady=5, sticky='e')

        vcmd = (self.master.register(self.voting_functions.validate_name), '%P')

        self.name_entry = tk.Entry(self.master, validate='key', validatecommand=vcmd)
        self.name_entry.grid(row=0, column=1, pady=5, sticky='w')

        self.candidate_menu_label = tk.Label(self.master, text='CANDIDATE MENU')
        self.candidate_menu_label.grid(row=1, column=0, columnspan=2, pady=10, sticky='n')

        self.create_vote_button(1, 'John')
        self.create_vote_button(2, 'Jane')
        self.create_vote_button(3, 'Jack')
        self.create_vote_button(4, 'Jill')

        self.exit_button = tk.Button(self.master, text='Exit', command=self.master.destroy)
        self.exit_button.grid(row=5, column=0, columnspan=2, pady=10, sticky='s')

        # Configure columns and rows to center content
        for i in range(6):
            self.master.columnconfigure(i, weight=1)
        for i in range(6):
            self.master.rowconfigure(i, weight=1)

    def create_vote_button(self, candidate: int, candidate_name: str) -> None:
        """
        Create a vote button for a candidate.

        Parameters:
            candidate (int): The candidate number.
            candidate_name (str): The candidate's name.
        """
        button = tk.Button(self.master, text=f'Vote for {candidate_name}', command=lambda: self.voting_functions.vote(candidate, self.name_entry))
        button.grid(row=candidate + 1, column=candidate % 2, padx=10, pady=5, sticky=('e', 'w'))

def main() -> None:
    """
    Run the main VotingApp program.
    """
    try:
        root = tk.Tk()
        voting_functions = VotingAppFunctions()
        app = VotingAppGUI(root, voting_functions)
        root.mainloop()

        # After the GUI exits, you can access the vote results
        print("Vote Results:", voting_functions.get_candidate_votes())
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

if __name__ == '__main__':
    main()

