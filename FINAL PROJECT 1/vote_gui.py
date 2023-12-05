import tkinter as tk
from tkinter import messagebox

class VotingApp:
    def __init__(self, master: tk.Tk) -> None:
        """
        Initialize the VotingApp.

        Parameters:
            master (tk.Tk): The root Tkinter window.
        """
        self.master: tk.Tk = master
        self.master.title("Voting App")

        # Disable resizing
        self.master.resizable(False, False)

        self.can1_votes: int = 0
        self.can2_votes: int = 0
        self.can3_votes: int = 0
        self.can4_votes: int = 0

        self.create_widgets()

    def validate_name(self, name: str) -> bool:
        """
        Validate the entered name.

        Parameters:
            name (str): The entered name.

        Returns:
            bool: True if the name is valid, False otherwise.
        """
        if any(char.isdigit() for char in name):
            messagebox.showwarning("Invalid Name", "Name cannot contain numeric characters.")
            return False
        return True

    def create_widgets(self) -> None:
        """
        Create the GUI widgets for the VotingApp.
        """
        self.name_label: tk.Label = tk.Label(self.master, text='Your Name:')
        self.name_label.grid(row=0, column=0, pady=5, sticky='e')

        vcmd: tuple = (self.master.register(self.validate_name), '%P')

        self.name_entry: tk.Entry = tk.Entry(self.master, validate='key', validatecommand=vcmd)
        self.name_entry.grid(row=0, column=1, pady=5, sticky='w')

        self.candidate_menu_label: tk.Label = tk.Label(self.master, text='CANDIDATE MENU')
        self.candidate_menu_label.grid(row=1, column=0, columnspan=2, pady=10, sticky='n')

        self.button1: tk.Button = tk.Button(self.master, text='Vote for John', command=lambda: self.vote(1))
        self.button1.grid(row=2, column=0, padx=10, pady=5, sticky='e')

        self.button2: tk.Button = tk.Button(self.master, text='Vote for Jane', command=lambda: self.vote(2))
        self.button2.grid(row=2, column=1, padx=10, pady=5, sticky='w')

        self.button3: tk.Button = tk.Button(self.master, text='Vote for Jack', command=lambda: self.vote(3))
        self.button3.grid(row=3, column=0, padx=10, pady=5, sticky='e')

        self.button4: tk.Button = tk.Button(self.master, text='Vote for Jill', command=lambda: self.vote(4))
        self.button4.grid(row=3, column=1, padx=10, pady=5, sticky='w')

        self.exit_button: tk.Button = tk.Button(self.master, text='Exit', command=self.master.destroy)
        self.exit_button.grid(row=4, column=0, columnspan=2, pady=10, sticky='s')

        # Configure columns and rows to center content
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.master.rowconfigure(2, weight=1)
        self.master.rowconfigure(3, weight=1)
        self.master.rowconfigure(4, weight=1)

    def vote(self, candidate: int) -> None:
        """
        Register a vote for the specified candidate.

        Parameters:
            candidate (int): The candidate for whom the vote is registered.
        """
        try:
            voter_name: str = self.name_entry.get()

            if not self.validate_name(voter_name):
                return

            if not voter_name:
                messagebox.showwarning("Missing Name", "Please enter your name before voting.")
                return

            if candidate == 1:
                messagebox.showinfo("Vote", f'{voter_name} voted for John')
                self.can1_votes += 1
            elif candidate == 2:
                messagebox.showinfo("Vote", f'{voter_name} voted for Jane')
                self.can2_votes += 1
            elif candidate == 3:
                messagebox.showinfo("Vote", f'{voter_name} voted for Jack')
                self.can3_votes += 1
            elif candidate == 4:
                messagebox.showinfo("Vote", f'{voter_name} voted for Jill')
                self.can4_votes += 1

            # Clear the content of the name entry
            self.name_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

def main() -> None:
    """
    Run the main VotingApp program.
    """
    try:
        root: tk.Tk = tk.Tk()

        # Set the initial size of the window
        root.geometry("400x300")

        app: VotingApp = VotingApp(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

if __name__ == '__main__':
    main()
