# voting_functions.py
import tkinter as tk
from tkinter import messagebox

class VotingAppFunctions:
    def __init__(self):
        self.can1_votes = 0
        self.can2_votes = 0
        self.can3_votes = 0
        self.can4_votes = 0

    def validate_name(self, name: str) -> bool:
        if any(char.isdigit() for char in name):
            messagebox.showwarning("Invalid Name", "Name cannot contain numeric characters.")
            return False
        return True

    def vote(self, candidate: int, name_entry: tk.Entry) -> None:
        try:
            voter_name = name_entry.get()

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
            name_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

    def candidate_menu(self) -> int:
        while True:
            try:
                print('----------------------\nCANDIDATE MENU\n----------------------')
                print('1 - John')
                print('2 - Jane')
                print('3 - Jack')
                print('4 - Jill')
                choice = int(input('Candidate: '))
                if 1 <= choice <= 4:
                    return choice
                else:
                    print('Invalid choice. Please enter a number between 1 and 4.')
            except ValueError:
                print('Invalid input. Please enter a valid integer (1, 2, 3, or 4).')

    def vote_menu(self) -> str:
        while True:
            try:
                print('---------\nVOTE MENU\n---------')
                print('v: VOTE\nx: Exit')
                option = input('Option: ').strip().lower()
                if option in ('v', 'x'):
                    return option
                else:
                    print('Invalid option. Please enter either "v" for vote or "x" for exit.')
            except Exception:
                print('An unexpected error occurred.')
